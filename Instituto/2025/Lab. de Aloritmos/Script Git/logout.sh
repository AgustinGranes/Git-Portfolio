git config --global --unset user.name
git config --global --unset user.email
git config --global --unset credential.helper
cmdkey /delete:LegacyGeneric:target=git:https://github.com

git config --global --replace-all user.name "AgustinGranes"
git config --global --replace-all user.email "agranes@alumno.huergo.edu.ar" 