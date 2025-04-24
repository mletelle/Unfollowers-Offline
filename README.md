# Unfollowers Instagram - Comparador de Seguidos/Seguidores 


> Averiguá de forma sencilla quiénes no te siguen (o a quiénes no seguís) en Instagram.
> Todo corre en tu PC, por lo que no es baneable ni hay peligro de que roben tu informacion (saludos para las app de PlayStore)

---

## 1. ¿Qué hace esto?

1. **Le pedís a Instagram** dos archivos (“followers” y “following”) que contienen tu lista de seguidos y seguidores.  
2. **Abrís** → seleccionás esos archivos.  
3. Se te muestra:  
   * Usuarios a los que seguís **y NO te siguen** de vuelta.  
   * Usuarios que te siguen **y VOS no seguís**.

---

## 2. Cómo obtener los archivos desde Instagram

1. **Desde el celular**  
   1. Abrí Instagram >  ☰  (Menú) > **Tu actividad**.  
   2. Elegí **Descargar tu información**.  
   3. Escribí tu e‑mail, tocá **Siguiente** y pedí **JSON** como formato.  
   4. Instagram te enviará un enlace por correo (puede tardar varios minutos).  
   5. Descargá el ZIP, descomprimilo y buscá dentro la carpeta **`followers_and_following`**.  
      * ***followers_1.json***  
      * ***following.json***

2. **Desde la web (PC)**  
   1. Entrá a [instagram.com](https://instagram.com) y logueate.  
   2. Click en tu avatar > **Configuración**.  
   3. **Privacidad y seguridad** > **Descargar datos**.  
   4. Ingresá tu e‑mail, elegí **JSON** y “Siguiente”.
   5. Instagram te envia un enlace por correo
   6. Descargá el ZIP, descomprimilo y buscá dentro la carpeta **`followers_and_following`**.  
      * ***followers_1.json***  
      * ***following.json***

> ⚠️ No renombres los archivos; el programa los detecta tal cual.

---

## 3. Opciones para usar la herramienta

### Opción A – Navegador sin instalar nada (Cualquier SO)
1. Descargá el archivo `index.html` (y la carpeta `scr/` si queres tener un loguito lindo)
2. Abri `index.html` (o arrastralo a tu navegador)
3. Listo, elegi primero `followers_1.json` y luego `following.json`.  
4. Revisá los link que te genera al perfil de cada persona.
5. Tuki

### Opción B: Script simple en Phyton 
1. Baja el archivo `comparar_instagram.py`
2. Tenes que tener `followers_1.json` y `following.json` en la misma carpeta que el **.py**
3. Corre el script: `python3 comparar_instagram.py`
4. Listo, te sale todo por consola ¯\_(ツ)_/¯

---

## Preguntas frecuentes
- ¿Se envían mis datos a algún servidor?	
No. Todo corre localmente en tu computadora.
- ¿Corre peligro mi informacion o mi cuenta?
Ninguno, fijate el `comparar_instagram.py`, mas claro echale agua.
- ¿Seguro?
Si.
- ¿Por qué pide JSON y no CSV/HTML?	
Porque Instagram ofrece la información más completa en JSON. Y es mas facil ¯\_(ツ)_/¯
- ¿Puedo borrar los archivos luego?
Sí, después de ejecutar podés eliminarlos. Literamente no guarda nada, asi que borralo noma'.
- ¿Hace falta cuenta de desarrollador en Instagram?
No.

---

## Licencia
Son un par de lineas en Python o HTML flaco. Usalo, modificá y compartí libremente.
*Dos besitos porque tres es mucha plata*
