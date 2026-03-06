#!/usr/bin/env python3
import sys
import re
import os
from docx import Document  # pip install python-docx

def main():
    docx_file = 'comandos.docx'
    
    # Test 1: Archivo existe
    if not os.path.exists(docx_file):
        print("❌ FAIL: No existe comandos.docx")
        sys.exit(1)
    
    # Extraer texto del .docx
    try:
        doc = Document(docx_file)
        content = '\n'.join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"❌ FAIL: Error leyendo .docx: {e}")
        sys.exit(1)
    
    # Test 2: Longitud mínima (al menos 1000 caracteres)
    if len(content) < 1000:
        print(f"❌ FAIL: Muy corto ({len(content)} chars). Mínimo 1000.")
        sys.exit(1)
    
    # Test 3: Comandos CMD
    cmd_comandos = ['mkdir', 'cd', 'dir', 'copy', 'del', 'cls']
    cmd_encontrados = sum(1 for cmd in cmd_comandos if re.search(rf'\b{cmd}\b', content, re.IGNORECASE))
    
    # Test 4: Comandos Git
    git_comandos = ['git clone', 'git init', 'git add', 'git commit', 'git push', 'git pull', 'git status']
    git_encontrados = sum(1 for git_cmd in git_comandos if git_cmd.lower() in content.lower())
    
    # Puntuación
    puntaje_cmd = min(cmd_encontrados / len(cmd_comandos) * 4, 4)
    puntaje_git = min(git_encontrados / len(git_comandos) * 4, 4)
    puntaje_longitud = 2
    
    total = puntaje_cmd + puntaje_git + puntaje_longitud
    
    print(f"📊 **Puntuación: {total:.1f}/10**")
    print(f"📄 Caracteres: {len(content)}")
    print(f"💻 CMD encontrados: {cmd_encontrados}/{len(cmd_comandos)} ({puntaje_cmd:.1f} pts)")
    print(f"🐙 Git encontrados: {git_encontrados}/{len(git_comandos)} ({puntaje_git:.1f} pts)")
    
    if total >= 7:
        print("✅ PASS")
        sys.exit(0)
    else:
        print("❌ FAIL - Revisa comandos faltantes")
        sys.exit(1)

if __name__ == "__main__":
    main()
