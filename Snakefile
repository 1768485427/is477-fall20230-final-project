rule prepare:
    output:
        "data/wine/wine.data"
    shell:
        "python scripts/prepare_data.py"

rule profile:
    input:
        "data/wine/wine.data"
    output:
        "profiling/report.html"
    shell:
        "python scripts/profile.py"

rule analyze:
    input:
        "data/wine/wine.data"
    output:
        "results/less_avg_alco.csv",
        "results/less_avg_malicacid.csv",
        "results/more_or_equal_avg_alco.csv",
        "results/more_or_equal_avg_malicacid.csv",
        "results/less_avg_Acalinity.csv",
        "results/less_avg_ash.csv",
        "results/less_avg_Color_intensity.csv",
        "results/less_avg_Flavanoids.csv",
        "results/less_avg_Hue.csv",
        "results/less_avg_Magnesium.csv",
        "results/less_avg_Nonglavanoid_phenols.csv",
        "results/less_avg_phenols.csv",
        "results/less_avg_Proanthocyanins.csv",
        "results/less_avg_Proline.csv",
        "results/more_or_equal_avg_Acalinity.csv",
        "results/more_or_equal_avg_ash.csv",
        "results/more_or_equal_avg_Color_intensity.csv",
        "results/more_or_equal_avg_Hue.csv",
        "results/more_or_equal_avg_Magnesium.csv",
        "results/more_or_equal_avg_Nonglavanoid_phenols.csv",
        "results/more_or_equal_avg_phenols.csv",
        "results/more_or_equal_avg_Proanthocyanins.csv",
        "results/more_or_equal_avg_Proline.csv",
        "results/more_or_equal_avg_Flavanoids.csv"
    shell:
        "python scripts/analysis.py"