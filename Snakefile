rule prepare:
    output:
        "data/wine/wine.data"
    shell:
        "python scripts/prepare_data.py"

rule profile:
    input:
        "data/wine/wine.data"
    output:
        "profilling/report.html"
    shell:
        "python scripts/profiles.py"

rule analyze:
    input:
        "data/wine/wine.data"
    output:
        "less_avg_alco.csv",
        "less_avg_malicacid.csv",
        "more_or_equal_avg_alco.csv"
    shell:
        "python scripts/analysis.py"

rule reproduce:
    input:
        "profilling/report.html",
        "less_avg_alco.csv",
        "less_avg_malicacid.csv",
        "more_or_equal_avg_alco.csv"