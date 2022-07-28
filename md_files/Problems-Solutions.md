# Problems:=>

1. **How to add all .pyc files in gitignore?**
     =First, make sure that you don't have any changes to commit;
        
    1.Edit or create your .gitignore and put the follow code:
            
            *.log

            *.pot

            *.pyc

            */*/*/__pycache__/

            */*/__pycache__/

            */__pycache__/

    2.Save -> git add . -> git commit
    3.'Clean Git Hub Cache' for your repo:
        git rm -rf --cached .
        git add .
        git commit -m "message"
    Commit and it's done!
    
    
    > **[IMPORTANT]**
    > git rm -rf --cached .This command cleans cached files and that's why after that line we need to stage all the file.This is done when you alrady added .pyc filed to staging area then we need to remove those files from this area and that's when removing cache command is used.


2. **Adding env file to gitignore**
    =>.env in gitignore first and then these steps
        a. git rm -f .env
        b. git add .
        c. git commit -m "remove .env file from git"
        d. git push