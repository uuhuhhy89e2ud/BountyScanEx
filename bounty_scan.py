import argparse
from modules import subdomain_enum, live_host, url_collector, param_fuzzer, vuln_scan, exploit_engine, report_gen

def main():
    parser = argparse.ArgumentParser(description="BountyScanEx - Auto Scan & Exploit Tool for Bug Bounty")
    parser.add_argument("-d", "--domain", help="Target domain", required=True)
    args = parser.parse_args()

    print("[*] Enumerating Subdomains...")
    subs = subdomain_enum.run(args.domain)

    print("[*] Filtering live hosts...")
    live = live_host.run(subs)

    print("[*] Collecting URLs from live subdomains...")
    urls = url_collector.run(live)

    print("[*] Fuzzing for parameter-based vulnerabilities...")
    param_vulns = param_fuzzer.run(urls)

    print(f"[*] Running nuclei scan on {len(live)} live hosts...")
    nuclei_results = vuln_scan.run(live)

    print("[*] Attempting auto exploitation...")
    auto_exploits = exploit_engine.run(nuclei_results)

    print("[*] Generating final report...")
    report_gen.generate(auto_exploits + param_vulns)

if __name__ == "__main__":
    main()
