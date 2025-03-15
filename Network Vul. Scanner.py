import nmap
import requests
import json

# Initialize the nmap scanner
scanner = nmap.PortScanner()

def scan_network(target):
    """Scan the target network or system for open ports and services."""
    print(f'Scanning {target}...')
    scanner.scan(target, arguments='-sV')  # -sV detects service versions
    return scanner

def check_vulnerabilities(service_name, service_version):
    """Check for known vulnerabilities in the identified services."""
    url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?keyword={service_name} {service_version}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        try:
            vulnerabilities = response.json()
            return vulnerabilities.get("result", {}).get("CVE_Items", [])
        except json.JSONDecodeError:
            print(f"Error decoding JSON response for {service_name} {service_version}")
            return []
        
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return []

def generate_report(scan_results):
    """Generate a report of identified vulnerabilities and remediation steps."""
    report = []

    for host in scan_results.all_hosts():
        report.append(f"Host: {host} ({scan_results[host].hostname()})")
        for proto in scan_results[host].all_protocols():
            lport = scan_results[host][proto].keys()
            for port in lport:
                service = scan_results[host][proto][port]['name']
                version = scan_results[host][proto][port]['version']
                report.append(f"Port: {port} | Service: {service} | Version: {version}")

                # Check for vulnerabilities
                vulns = check_vulnerabilities(service, version)
                if vulns:
                    report.append("Vulnerabilities found:")
                    for vuln in vulns:
                        cve_id = vuln['cve']['CVE_data_meta']['ID']
                        description = vuln['cve']['description']['description_data'][0]['value']
                        report.append(f"- {cve_id}: {description}")
                else:
                    report.append("No known vulnerabilities found.")

    return "\n".join(report)

def main():
    # User input for target network or system
    target = input("Enter the target IP address or network (e.g., 192.168.1.0/24): ")
    
    # Scan the target network
    scan_results = scan_network(target)

    # Generate vulnerability report
    report = generate_report(scan_results)
    
    # Save report to file
    report_file = "vulnerability_report.txt"
    with open(report_file, 'w') as f:
        f.write(report)

    print(f"Vulnerability report saved to {report_file}")

if __name__ == "__main__":
    main()
