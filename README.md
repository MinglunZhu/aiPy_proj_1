# aiPy_proj_1

##Description
This is the project I did for Udacity Course AI Programming with Python Project 1 - Use A Pre-trained Image Classifier to Identify Dog Breeds.

It's a python commandline program that allows you to choose between 3 network architectures (ResNet, AlexNet, or VGG) and the folder containing the images you want to classify. The images must be labeled by it's file name, examples included in the `pet_images` folder.

This label will be used to measure the accuracy of the chosen network architecture. The program will also measure the time cost for running each network architecture. The result will be printed into a text file.

##How to use
Download the files, then in your commanline interface, run the following code:
```
python check_images.py --help
```
which shows you the arguments you can supply. These arguments defaults to the files supplied in this repository if you don't supply one.

```
sh run_models_batch.sh
```
Runs all three models on the images in the default folder `pet_images`.

```
sh run_models_batch_uploaded.sh
```
Runs all three models on the images in the uploaded folder `uploaded_images`.

results are printed to a text file in the format of `architecture_folder.txt`.
E.g `alexnet_pet-images.txt`, `alexnet_uploaded-images.txt`

##License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
