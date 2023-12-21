Primero he creado el ejemplo.py con la suma y resta de dos números.

Luego he creado los alias globales:
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

Y también los alias locales:
git config alias.co checkout
git config alias.br branch
git config alias.ci commit
git config alias.st status

He creado dos nuevas ramas y las he subido remotamente. Sus nombres son "nueva-rama" y "nuevisima-rama".

Para usar bisect he cambiado el numero 2, por una cadena "2" y he hecho commit con este error.
Al ejecutar me da error y entonces hago el "git bisect start" y marco el commit actual como malo con "git bisect bad".
Luego, marco con "git bisect good <hash>" el commit inicial que es correcto y funciona. Y por último finalizo con "git bisect reset".
Ahora que ya sé que el commit actual es el único erroneo, hago "git reset --hard" para eliminar el commit.

Por último, creado en .git/hooks/ un hook "pre-commit" que al ejecutar un comando "git commit" antes de realizar este comando, muestra
un mensaje de advertencia.

El repositorio en github es: https://github.com/nmp50-ua/Practica-9-DCA
