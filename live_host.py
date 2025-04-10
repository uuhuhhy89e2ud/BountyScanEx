import subprocess

def run(subdomains):
    live = []
    for sub in subdomains:
        try:
            cmd = f"httpx -silent -timeout 5 -no-color -status-code -title -u https://{sub}"
            output = subprocess.check_output(cmd, shell=True).decode()
            if "200" in output or "302" in output:
                live.append(sub)
        except:
            pass
    return live
