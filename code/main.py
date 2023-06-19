import imageio.v3

file_names= ["sincapSol.png","sincapSağ.png"] #gif oluşturacağımız resimleri bu listeye koyuyoruz
images = [] #boş bir liste oluşturuyoruz. Buraya oluşturduğumuz gif i ekleyeceğiz

for filename in file_names: #for döngüsüyle
    images.append(imageio.v3.imread(filename)) #imageio'nun imread özelliği belirttiğimiz resimleri okumasını sağlıyor

imageio.mimwrite("sincap.gif", images, format="GIF", duration=0.5, loop= 10)#iamgeio'nun mimwrite özelliği sayesinde belirlediğimiz uriye resmi yazdırıyoruz
