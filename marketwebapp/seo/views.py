from django.shortcuts import render


# from python_seo_analyzer.seoanalyzer.analyzer import analyze
from seoanalyzer import analyzer


def index(request):
    if request.method == "GET":
        return render(request, "seo/index.html")
    if request.method == "POST":
        website = request.POST["websitetoseo"]
        print("query is: ", website)
        output = analyzer.analyze(website)
        print(output["pages"][0]["warnings"])
        return render(request, "seo/result.html", {"result": output})

