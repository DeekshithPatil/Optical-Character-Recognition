from wand.image import Image as wi
pdf = wi(filename="hdfc.pdf", resolution=350)
pdfimage = pdf.convert("jpeg")
i=1
for img in pdfimage.sequence:
    page = wi(image=img)
    page.save(filename=str(i)+".jpg")
    i +=1