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
        "more_or_equal_avg_alco.csv",
        "more_or_equal_avg_malicacid.csv",
        "less_avg_Acalinity.csv",
        "less_avg_ash.csv",
        "less_avg_Color_intensity.csv",
        "less_avg_Flavanoids.csv",
        "less_avg_Hue.csv",
        "less_avg_Magnesium.csv",
        "less_avg_Nonglavanoid_phenols.csv",
        "less_avg_phenols.csv",
        "less_avg_Proanthocyanins.csv",
        "less_avg_Proline.csv",
        "more_or_equal_avg_Acalinity.csv",
        "more_or_equal_avg_ash.csv",
        "more_or_equal_avg_Color_intensity.csv",
        "more_or_equal_avg_Hue.csv",
        "more_or_equal_avg_Magnesium.csv",
        "more_or_equal_avg_Nonglavanoid_phenols.csv",
        "more_or_equal_avg_phenols.csv",
        "more_or_equal_avg_Proanthocyanins.csv",
        "more_or_equal_avg_Proline.csv",
        "more_or_equal_avg_Flavanoids.csv"
    shell:
        "python scripts/analysis.py"

rule reproduce:
    input:
        "profilling/report.html",
        "less_avg_alco.csv",
        "less_avg_malicacid.csv",
        "more_or_equal_avg_alco.csv",
        "more_or_equal_avg_malicacid.csv",
        "less_avg_Acalinity.csv",
        "less_avg_ash.csv",
        "less_avg_Color_intensity.csv",
        "less_avg_Flavanoids.csv",
        "less_avg_Hue.csv",
        "less_avg_Magnesium.csv",
        "less_avg_Nonglavanoid_phenols.csv",
        "less_avg_phenols.csv",
        "less_avg_Proanthocyanins.csv",
        "less_avg_Proline.csv",
        "more_or_equal_avg_Acalinity.csv",
        "more_or_equal_avg_ash.csv",
        "more_or_equal_avg_Color_intensity.csv",
        "more_or_equal_avg_Hue.csv",
        "more_or_equal_avg_Magnesium.csv",
        "more_or_equal_avg_Nonglavanoid_phenols.csv",
        "more_or_equal_avg_phenols.csv",
        "more_or_equal_avg_Proanthocyanins.csv",
        "more_or_equal_avg_Proline.csv",
        "more_or_equal_avg_Flavanoids.csv"