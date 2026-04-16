
---
title: Sortinigdemo
emoji: 🤍
colorFrom: pink
colorTo: purple
sdk: gradio
sdk_version: 6.12.0
app_file: app.py
pinned: false
short_description: this is the final project for CISC 121
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
# Shuttle Stop Crowd Ranking with Merge Sort

## Chosen Problem
The problem that I chose was (3) Shuttle Stop Crowd Ranking. I will be making an app that ranks campus shuttle stops by crowd count to help decide where an extra shuttle should be sent.

## Chosen Algorithm
I will be using Merge Sort because it is efficient and easy to visualize through repeated splitting and merging of lists. Not only it is a clear and efficient way to sort the stops by crowd count, but it also makes the step-by-step process easier for users to follow. Since the dataset is a list of shuttle stops with crowd counts, merge Sort will work well because it can sort these records by crowd count while making each merge step visible to the user. However, it is important that there are two preconditions for this app, and that is crowd counts must be integers, stop names cannot be empty. Users will see the original stop list, each merge step and the final ranked list.

## Demo
Since the file for edge cases testing is too big, it will be stored in HuggingFace.
![1](1.png)
![2](2.png)
![3](3.png)
![4](4.png)

## Problem Breakdown & Computational Thinking
### Decomposition
1. The user enters the input of shuttle stop names and crowd counts into the app.
2. The app checks whether the input is in the correct format and whether the crowd counts are valid numbers.
3. The data is separated into smaller lists as Merge Sort begins splitting the shuttle stops.
4. The app compares and merges the smaller lists back together in sorted order.
5. The final ranked list and the step-by-step sorting process are shown to the user.

### Pattern Recognition
- The app repeatedly divide the list into smaller halves
- The app repeatedly compare two front elements during merge

### Abstraction
- Show list changes after each merge
- Hide low-level memory details

### Algorithm Design
The app follows a simple input-process-output design. The user will first enter shuttle stop names and crowd counts, then then program checks the input and applies merge sort. It will further show the sorted ranking along with the sorting steps. This makes the app easy to use because the user can clearly see how their input is turned into the final result.

### Flowchart
![CISC 121 Project](./CISC%20121%20Project.drawio.png)

## Steps to Run
1. Install dependencies
2. Run app.py

## Requirements
- gradio

## Hugging Face Link
[(paste link)](https://huggingface.co/spaces/meganongg/sortinigdemo)

## Testing
- normal input
- duplicate values
- empty list

## Author & Acknowledgment
AI usage & sources disclosure: ChatGPT 5.4 was used to assist with troubleshooting issues related to codes and Gradio. Google Germini AI was also used to assist with troubleshooting and coding related issues.

Sources for Image and Music: Merge Sort Tree Diagram: 
Background Music: [ NO COPYRIGHT ] LO-FI CUTE BACKGROUND MUSIC from BLUE~ LITTLE BUNNY https://youtu.be/Su4AYa5X8a0?si=7LBCJgyVGKnCsRD0
Kuromi Gif: https://cults3d.com/en/3d-model/art/kuromi-from-sanrio-sitting-pose
