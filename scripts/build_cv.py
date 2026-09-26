from pathlib import Path
import sys
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
root=Path(__file__).resolve().parents[1]
out=Path(sys.argv[1]) if len(sys.argv) > 1 else root/'assets/cv/Francisco_Arano_CV_Full_Stack_ATS.pdf'
out.parent.mkdir(parents=True,exist_ok=True)
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameCV',fontName='Helvetica-Bold',fontSize=18,leading=21,alignment=TA_CENTER,textColor=colors.HexColor('#153c35'),spaceAfter=5))
styles.add(ParagraphStyle(name='RoleCV',fontName='Helvetica-Bold',fontSize=10.5,leading=14,alignment=TA_CENTER,spaceAfter=5))
styles.add(ParagraphStyle(name='ContactCV',fontName='Helvetica',fontSize=8.6,leading=12,alignment=TA_CENTER,spaceAfter=3))
styles.add(ParagraphStyle(name='SectionCV',fontName='Helvetica-Bold',fontSize=10,leading=13,spaceBefore=10,spaceAfter=5,textColor=colors.HexColor('#153c35'),borderWidth=0,borderPadding=0))
styles.add(ParagraphStyle(name='BodyCV',fontName='Helvetica',fontSize=9.1,leading=12.5,spaceAfter=4))
styles.add(ParagraphStyle(name='BulletCV',parent=styles['BodyCV'],leftIndent=9,firstLineIndent=-7,spaceAfter=5))
story=[]
def p(text,style='BodyCV'): story.append(Paragraph(text,styles[style]))
def section(t): p(t,'SectionCV')
p('FRANCISCO LEONARDO ARANO HERRERA','NameCV')
p('Backend / Full Stack Developer | Node.js · NestJS · TypeScript','RoleCV')
p('Veracruz, México · (229) 250 86 12 · aranoherrera92@gmail.com','ContactCV')
p('<link href="https://www.linkedin.com/in/francisco-leonardo-arano-herrera-540198169/">LinkedIn</link> · <link href="https://github.com/FLAranoHerrera">GitHub</link> · <link href="https://gitlab.com/FLAranoHerrera">GitLab</link> · <link href="https://flaranoherrera.github.io/mi-portfolio/">Portfolio</link>','ContactCV')
section('PERFIL PROFESIONAL')
p('Desarrollador Full Stack con enfoque backend y experiencia en una plataforma SaaS de transporte público. Integro sistemas legacy con NestJS, normalizo datos operativos y desarrollo interfaces administrativas con Next.js. Experiencia con APIs REST, PostgreSQL, MongoDB, MQTT, Docker y DigitalOcean.')
section('EXPERIENCIA PROFESIONAL')
p('<b>Desarrollador Full Stack / Analista Programador — Peek Softworks</b><br/>Noviembre 2025 - actualidad · Boca del Río, Veracruz')
p('• <b>Integración legacy:</b> implementé de forma individual la integración mediante MQTT entre un backend Express/MongoDB y el nuevo backend NestJS. Normalicé nombres de unidades y cobros del sistema anterior para hacerlos consumibles desde el nuevo backend.','BulletCV')
p('• <b>Mapas operativos:</b> corregí en el frontend Next.js un problema de renderizado de iconos de autobuses en OpenStreetMap y Google Maps, restableciendo la visualización de las unidades.','BulletCV')
p('• <b>Portal administrativo:</b> construí un portal para cadenas comerciales que permite gestionar llaves para recargas, expedir tarjetas NFC y consultar su saldo.','BulletCV')
p('Trabajo adicional con APIs, autenticación, despliegues Docker en DigitalOcean, Azure Key Vault y almacenamiento MinIO.')
section('PROYECTOS SELECCIONADOS')
p('<b><link href="https://github.com/FLAranoHerrera/ecommcerce_m4">Backend Ecommerce — API individual de compras</link></b> | NestJS, PostgreSQL, TypeORM, Jest<br/>Compras transaccionales, bloqueo de productos, autorización por propietario y rol, migraciones y pruebas automatizadas con GitHub Actions. Documentación Swagger y despliegue con Docker/Render.')
p('<b><link href="https://github.com/lienzoculinariog2/nuevolienzoback-">Lienzo Culinario — Ecommerce colaborativo</link></b> | NestJS, Stripe, Auth0, Cloudinary<br/>Proyecto académico en equipo. Mi aportación se centró en el backend: pagos, autenticación y recursos multimedia; otros integrantes desarrollaron el frontend.')
p('<b><link href="https://github.com/FLAranoHerrera/sushi-pos-backend">Sushi POS — Punto de venta en desarrollo</link></b> | NestJS, Next.js, PostgreSQL<br/>Servicios para usuarios, productos, categorías y órdenes. Demo frontend con datos ficticios, creación y cancelación de órdenes y cobros simulados; sin transacciones de pago reales.')
section('HABILIDADES TÉCNICAS')
p('<b>Backend y datos:</b> Node.js, NestJS, Express, TypeScript, PostgreSQL, MongoDB, TypeORM, JWT.<br/><b>Frontend:</b> React, Next.js, Vue.js, HTML, CSS.<br/><b>Herramientas:</b> Git, Docker, DigitalOcean, Swagger, Jest, MQTT, MinIO, Azure Key Vault.<br/><b>Integraciones:</b> Stripe, Auth0, Cloudinary, OpenStreetMap, Google Maps y NFC.')
section('EDUCACIÓN Y FORMACIÓN')
p('<b>Full Stack Web Developer — Henry</b> | Marzo - agosto 2025<br/><b>Licenciatura en Criminología y Criminalística — CLEU</b> | 2010 - 2015<br/><b>Técnico Informático — CBTIS No. 66</b> | 2007 - 2010')
p('Formación complementaria: Flutter y Dart (Udemy, 2025); introducción a Python (Santander Open Academy, 2024).')
section('EXPERIENCIA ADICIONAL E IDIOMAS')
p('Fundador y responsable de operaciones, Cervecería Igriega (2020-2024) · Docente universitario, CLEU (2018-2020) · Atención de emergencias 911, Secretaría de Seguridad Pública (2015-2019).<br/><b>Español:</b> nativo · <b>Inglés:</b> B2')
doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=36,leftMargin=36,topMargin=30,bottomMargin=28,title='Francisco Arano | Backend / Full Stack Developer',author='Francisco Leonardo Arano Herrera')
doc.build(story)
print(out)
