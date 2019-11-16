#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Minglun Zhu
# DATE CREATED: 2019-10-09                                 
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
#
def div_chk(x, y, r = 0):
  '''
    applies the normal division to input, but
    if if division by 0, then returns a default value instead of error
    
    params:
        x (int or float): left side of division
        y (int or float): right side of division
        r (any type): default value to be returned if division by zero (default 0)
        
    returns:
        division result or
        if division by zero then returns the specified return value (default 0)
  '''
  try:
    z = x / y
  except ZeroDivisionError:
    return r
  else:
    return z

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function
    imgCnt = len(results_dic)
    
    stats = {
        'n_images': imgCnt
    }
    
    dogImgCnt = 0
    matchCnt = 0
    correctDogCnt = 0
    correctNonDogCnt = 0
    correctDogBreedCnt = 0
    
    for v_list in results_dic.values():
        dogImgCnt += v_list[3]
        matchCnt += v_list[2]
        correctDogCnt += int(v_list[3] == v_list[4] == 1)
        correctNonDogCnt += int(v_list[3] == v_list[4] == 0)
        correctDogBreedCnt += int(v_list[3] == v_list[2] == 1)
    
    stats.update({
        'n_dogs_img': dogImgCnt,
        'n_notdogs_img': imgCnt - dogImgCnt,
        'n_match': matchCnt,
        'n_correct_dogs': correctDogCnt,
        'n_correct_notdogs': correctNonDogCnt,
        'n_correct_breed': correctDogBreedCnt,
        
        'pct_match': div_chk(matchCnt, imgCnt) * 100,
        'pct_correct_dogs': div_chk(correctDogCnt, dogImgCnt) * 100,
        'pct_correct_breed': div_chk(correctDogBreedCnt, dogImgCnt) * 100
    })
    
    stats['pct_correct_notdogs'] = div_chk(correctNonDogCnt, stats['n_notdogs_img']) * 100
    
    #test div chk function
    #print(div_chk(1, 0))
    #print(div_chk(1, 0, 'div by zero'))
    #print(div_chk(2, 2))
    
    return stats
