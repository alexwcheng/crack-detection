# Construction Deficiency Detection

![Deficiency-Detection-Demo](Web_Application/Deficiency-Detection-Demo.gif)

#
### Project File Summary

   - <b>[README.md](README.md)</b> - a summary of all contents in this repository.
   - <b>[/Images](/Images)</b> - Exported plots, etc...
   - <b>[/Jupyter_Notebooks](/Jupyter_Notebooks)</b> - All Jupyter Notebooks for this project.
   - <b>[/Py_Files](/Py_Files)</b> - .py files loaded / imported in the Jupyter Notebooks.
   - <b>[/Final_Presentation](/Final_Presentation)</b> - A non-technical presentation of the project.
   - <b>[/Web_Application](/Web_Application)</b> - Code + video demo of a simple proof-of-concept web-app that detects cracking.
   
#
### Project Members

   - <b>[Alex Cheng](https://github.com/alexwcheng)</b>

#
### Project Scenario

Architects and engineers visit construction sites regularly to observe general progress and identify deficient work. Photography is the primary way to document conditions on-site. If the project is large, then thousands of photos can be taken on a single visit. After the site visit, a field report is made that records general observations and identifies any deficient work. It is very time-consuming to to find all of the images that capture deficient work in order to generate a detailed and thorough field report.

So to make life easier, an automated tool powered by a Convolutional Neural Network (CNN) can help detect obviously deficient work for us - in particular, cracking. This tool is not intended to replace manual review of construction images completely, but would speed up the process significantly. In a large design firm, this tool would save thousands of hours of labor per year. This in turn saves hundreds of thousands of dollars, which means more profit and less mind-numbing work to be done by already overworked professionals.

#
### Project Goals

The goal of this project is to create an automated tool that can rapidly classify 3 things about a construction photo:

1. Is the photo "general" or "specific"?
2. What type of material is in the photo?
3. Is this material "cracked" or "not cracked"?

#
### Data 

I gathered a dataset of roughly 4,000 images of general construction progress photos, and photos focusing on common building materials seen on construction sites, including brick, concrete, drywall, glass, and tile. The dataset was built using combination of actual construction photos, web-scraped photos, and personal photography. In building this unique dataset, I tried to keep the dataset balanced in terms of "cracked" versus "not cracked" images. Since people take pictures of construction deficiencies at many different scales, I endeavored to collect a variety of photos with cracks of all sizes. 

One challenge to overcome is to have the crack be large or prominent enough in the photo for a human (or a computer) to detect it. So images of both "obvious" and "subtle" cracking were included in the dataset. Another challenge is "noise" in the photo - like people, or construction tools, or other visual distractions. So a range of images were included that introduce various amounts of visual "noise" to ensure that the CNN would pick up on cracking in both simple and more complex scenes.

#
### Evaluation Metrics

Next, I had to define the evaluation metrics for success. Missing deficiencies is potentially a safety issue. So arguably, the most important metric to evaluate "success" would be to measure **RECALL** and/or **FALSE NEGATIVE RATE.** However, we don't want to just classify all images as "deficient"...because then we wouldn't be saving architects and engineers any time or effort! So **F1-Score** is likely the best metric to measure instead since it balances precision and recall. To explain performance non-technically, I used accuracy since most already have an understanding of this metric.

#
### CNN Building + Training

• I built and trained 3 CNNs:

• One for "general" vs. "specific" classification.
   
• One for material type classification.
   
• One for "cracked" vs. "not cracked" classification.

#
### CNN Metrics

I analyzed confusion matrix results of the CNN models, then determined accuracy, precision, recall, and F1 score metrics. Next, I plotted prediction probabilities for each type of classification. Prediction probabiities are important in crack detection. Architects and engineers want to be certain that they are not missing any significant, potentially dangerous deficiencies. Otherwise, there will be a significant professional liability. So I determined a prediction probability "cutoff" point at which an image would need to be manually checked by a person, since the model is not "confident" enough in its prediction for architects and engineers to trust the prediction completely.

![Prediction_Probabilities](/Images/Prediction_Probabilities_Slide.jpg)

#
### Conclusions

• For every 1,000 images:

   • At a 90% prediction probability cutoff, we only have to manually check 140 images. (86% reduction of work.)
   
   • At a 95% prediction probability cutoff, we only have to manually check 200 images. (80% reduction of work.)
   
   • At a 99% prediction probability cutoff, we only have to manually check 310 images. (69% reduction of work.)

#
### Future Work

To improve this project, I would use images with even more “visual noise” to train on. Furthermore, I would consider more types of materials, such as plastics, wood, composites, or even rammed earth. Finally, I would spend more time training and tuning various layers of the CNNs to improve training metrics and reduce the loss function.
   
In the future, I would build more CNNs to detect other types of deficiencies besides cracking. Then we could combine these models to build a tool that can detect all types of construction deficiencies. In the further future, instead of people, maybe drones could take photos of construction sites! Using a more robust version of this tool, drones could auto-identify deficient work! This would save an even more tremendous amount of time and money for architecture, engineering, and construction firms.
