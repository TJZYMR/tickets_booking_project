1. When there is .ini or .env files,those files are for holding environment variables and are set at root directory.
2. if you want to use gitignore but dont want your local place to be changed then dont sync after commit in vscode,this way your local files will also be ignored and deleted.Just select push after commit in vscode.
3. git push origin <your_branch_name> -f
    this command is for forcing the push to the remote branch instead of pulling and then oushing again.Simple an sober.

4.JWTs are not meant to be used to store them in the database.Previously it was made to overcome the limitations of sessions which were being stored in the db.SO,It means cryptographically signed token is not stored in the database.