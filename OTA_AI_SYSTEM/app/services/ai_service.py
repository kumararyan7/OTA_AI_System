def analyze_logs(logs):
    analysis = []

    for log in logs:
        if "Failed" in log:
            analysis.append("Update failed: Possible network or installation issue")
        elif "Downloading" in log:
            analysis.append("Download phase executed")
        elif "Installing" in log:
            analysis.append("Installation in progress")

    if not analysis:
        return ["No significant events found"]

    return analysis
