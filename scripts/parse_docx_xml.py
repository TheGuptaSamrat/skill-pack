#!/usr/bin/env python3
"""Parse FPSL .docx by extracting and parsing raw XML"""

import xml.etree.ElementTree as ET
import zipfile
import re
from pathlib import Path

def extract_text_from_docx(docx_path):
    """Extract text from .docx by parsing XML"""
    
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        xml_content = zip_ref.read('word/document.xml')
    
    # Parse XML - namespace handling
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
    }
    
    root = ET.fromstring(xml_content)
    
    # Extract all paragraphs
    paragraphs = []
    for para in root.findall('.//w:p', namespaces):
        # Get paragraph properties/style
        pPr = para.find('w:pPr', namespaces)
        style = 'Normal'
        if pPr is not None:
            pStyle = pPr.find('w:pStyle', namespaces)
            if pStyle is not None:
                style = pStyle.get(f'{{{namespaces["w"]}}}val', 'Normal')
        
        # Extract text runs
        text_parts = []
        for t in para.findall('.//w:t', namespaces):
            if t.text:
                text_parts.append(t.text)
        
        text = ''.join(text_parts).strip()
        if text:
            paragraphs.append({
                'text': text,
                'style': style
            })
    
    return paragraphs

def main():
    docx_file = '/Users/samratgupta/skill-pack/metadata-drop/fpsl/Building SAP FPSL_FSDM Golden Source.docx'
    
    print("Parsing FPSL document...")
    paragraphs = extract_text_from_docx(docx_file)
    
    print(f"\n📄 Total paragraphs extracted: {len(paragraphs)}")
    
    # Show structure
    print(f"\n📋 Document Structure:\n")
    for i, p in enumerate(paragraphs[:100]):
        if 'Heading' in p['style'] or len(p['text']) < 80:
            print(f"{i+1:3}. [{p['style']:15}] {p['text'][:100]}")
    
    # Save to markdown
    md_path = '/Users/samratgupta/skill-pack/metadata-drop/fpsl/FPSL-Golden-Source-Extracted.md'
    with open(md_path, 'w') as f:
        f.write("# Building SAP FPSL/FSDM Golden Source\n\n")
        f.write("*Extracted from: Building SAP FPSL_FSDM Golden Source.docx*\n\n")
        
        for p in paragraphs:
            style = p['style']
            text = p['text']
            
            if 'Heading1' in style:
                f.write(f"# {text}\n\n")
            elif 'Heading2' in style:
                f.write(f"## {text}\n\n")
            elif 'Heading3' in style:
                f.write(f"### {text}\n\n")
            elif 'List' in style:
                f.write(f"- {text}\n")
            else:
                f.write(f"{text}\n\n")
    
    print(f"\n✅ Extracted content saved to: {md_path}")
    print(f"   Total lines: {len(paragraphs)}")
    print(f"\n   First 20 paragraphs:")
    for i, p in enumerate(paragraphs[:20]):
        print(f"   {i+1}. {p['text'][:70]}...")

if __name__ == '__main__':
    main()
