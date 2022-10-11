# Data Engineering with AWS Part 1
This is the repository for the LinkedIn Learning course Data Engineering with AWS Part 1. The full course is available from [LinkedIn Learning][lil-course-url].

![Data Engineering with AWS Part 1][lil-thumbnail-url] 

Businesses need data experts—now more than ever before. As data-driven decision-making has risen to boardroom prominence, the role of the data expert has become essential to understanding and scaling a business. In this course—the first in a two-part series—instructor Dipali Kulshrestha shows you how to get started on your professional journey and grow your career as a data engineer with AWS.

Get an introduction to the field of data engineering and why it’s so important in today’s business world. Explore a variety of data types, data lakes, data sources, and how to use built-in AWS components such as DynamoDB, Kinesis, and S3 to store and manage your streams. Find out how to leverage the full power of an end-to-end data engineering pipeline, from selecting and configuring ingestion patterns, to storing data for analytic processing with S3. Test your new skills along the way in the hands-on data challenges at the end of each section.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"


### Instructor

Dipali Kulshrestha 
                            


                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/dipali-kulshrestha).

[lil-course-url]: https://www.linkedin.com/learning/data-engineering-with-aws-part-1?dApp=59033956
[lil-thumbnail-url]: https://cdn.lynda.com/course/3010976/3010976-1664986900593-16x9.jpg
