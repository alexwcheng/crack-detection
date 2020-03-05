# Construction Deficiency Detection
This README.md lists project members, goals, responsibilities, and a summary of the files in the repository.

### Project File Summary

   - <b>[README.md](README.md)</b> - a summary of all contents in this repository.
   - <b>[/Images](/Images)</b> - Exported plots, etc...
   - <b>[/Jupyter_Notebooks](/Jupyter_Notebooks)</b> - All Jupyter Notebooks for this project.
   - <b>[/Py_Files](/Py_Files)</b> - .py files loaded / imported in the Jupyter Notebooks.
   - <b>[/Final_Presentation](/Final_Presentation)</b> - A non-technical presentation of the project.
   
### Project Members

   - <b>[Alex Cheng](https://github.com/alexwcheng)</b>

### Project Scenario

Architects and engineers visit construction sites regularly to observe general progress and identify deficient work. Photography is the primary way to document conditions on-site. If the project is large, then thousands of photos can be taken on a single visit. After the site visit, a field report is made that records general observations and identifies any deficient work. It is very time-consuming to to find all of the images that capture deficient work in order to generate a detailed and thorough field report.

So to make life easier, an automated tool powered by a Convolutional Neural Network (CNN) can help detect obviously deficient work for us. This tool is not intended to replace manual review of construction images completely, but would speed up the process significantly. In a large design firm, this tool would save thousands of hours of labor per year. This in turn saves hundreds of thousands of dollars, which means more profit and less mind-numbing work to be done by already overworked professionals.


### Project Goals

The goal of this project is to create an automated tool that can automatically classify 3 things about a construction photo:

1. Is the photo "general" or "specific"?
2. What type of material is in the photo?
3. Is this material "cracked" or "not cracked"?


### Methodology 

1. Gather a dataset of images of general construction progress photos, and photos focusing on common building materials seen on construction sites. The data collection includes a combination of actual construction photos, web-scraped photos, and personal photography).

2. Define the evaluation metrics for success. The most important thing is to capture ALL of the deficiencies, no matter what.
Missing deficiencies is potentially a safety issue. Arguably, the most important metric to evaluate "success" would be to measure RECALL and FALSE NEGATIVE RATE. However, we don't want to just classify all images as "deficient"...then we aren't saving architects and engineers any time or effort! So maybe we would consider using F1-Score instead since it balances accuracy and recall so the model doesn't just classify everything as deficient.

2. Create, train, and fine-tune CNN for "general" vs. "specific" classification.

3. Create, train, and fine-tune CNN for material type classification.

4. Create, train, and fine-tune CNN for "cracked" vs. "not cracked" classification.

5. Analyze prediction probabilities for each type of classification. Determine a prediction probability "cutoff" point at which an image would need to be manually checked by a person, since the model is not "confident" enough in its prediction.

6. Analyze confusion matrix results of the CNN models. Determine accuracy, precision, recall, and F1 score metrics. Determine a ratio of how often the model is correctly classifying "cracked" materials. That is what we care about most.

7. Design a presentation to cleanly and simply explain the findings of the modeling process.

### Project Responsibilities

   -  All project responsibilities were completed by <b>[Alex Cheng](https://github.com/alexwcheng)</b>.
