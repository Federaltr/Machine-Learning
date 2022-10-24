# Cloud Basics-AWS-EC2 

# MLDP-2 -- str 270
# MLDP-3 -- str 397
# MLDP-4 -- str 756

#%% MLDP-1 - CLOUD COMPUTING BASICS - Josh
# Table of Contents
    # Introduction to Cloud Computing
    # Why Cloud Computing?
        # Virtualization
        # Containerzation Techonology
        # Software Development Cycle
        # Serverless
    # Service Model
    # Deployment Models
    # Conculusion
    
# AWS hesabı açarken notlar
    # Email hesabınızla giriş yapacaksınız kendi e-mailiniz root user ınız. Root hesapla girmek tavsiye edilmiyor.
    # Iam user oluşturacağız. Onunla giriş yapacağız. AWS hesabını kullanacağımız hesap
    # Billing alarm oluşturacağız

# Introduction to Cloud Computing
    # Bir çiçeğimiz var. Bunu yetiştirmek için saksı,toprak su vs gibi ihtiyaçlarımız var
    # Bunlar çiçecin yetişmesi için bir altyapı.

# Çiçeğimiz bir yazılım aslında(Tulip.com mesela)(e-ticaret yazılımı, image optimizasyon yazılımı, 
# .. ML yazılımı gibi yazılımlar olabilir). Bu fikir olarak ortaya atılıyor.
# Sonra bu yazılım için gerekli olan şeylerden konuşuluyor. Sonra bu projenin bir dökümanı
# .. oluşturuluyor. Sonra bu döküman üzerinden buna bir product owner atanıyor. Developer takımları
# .. kuruluyor. Deveops takımlarını yönetecek kişiler tahsis ediliyor ve developerlar işe
# .. başlayıp tulip.com u ortaya çıkarıyorlar. Bunu kendi bilgisayarlarında çalıştırabiliyorlar
# .. Ama biz bunu dünya çapında kullanıcılara. Kullanıcılara bir değer katacak ve ben bundan bir fayda sağlayacağım
# Bu yazılımı bir şekilde web üzerinde yayınlamam lazım. Bu ülkesel ve global çapta olabilir sizin iş planınıza  bağlı

# 1.Toprak = Veritabanı : Günümüz modern yazılımlarımızda hep veritabanı var.
# 2.Saksı(Bu toprağı saksıya koymalıyız) = Server/Sunucu(Büyük/Kapsamlı bilgisayar)
# .. Bu siteyi insanlara sunmak için 24 saat açık bir bilgisayara ihtiyacım var çünkü
# .. insanlar buna bağlanacak. Elektrik kesildiğinde dahil çalışacak. Gelen istekleri de karşılayabilecek
# .. arkada dönen java, python arkada ne varsa artık bunlar için güçlü/Kapasiteli bir bilgisayara ihtiyacımız var 
# .. Bunu sunucu sağlayacak. Evimizdeki bilgisayarlar bunları karşılamaz
# .. Sunucuların ekranı olmaz. Bir kabinet üzerinde takılı olarak durur ve uzaktan bağlanıp komutlarla yönetirsiniz sunucuyu
# 3.Su(E-ticaret uygulamasını yayınlayabilmemiz için sunucu üzerinde bir program çalışması gerekiyor) 
# .. Bunlar Apache(Linux da çalışan), EngineX(Linux da), Microsoft ISS(Windows da çalışan)
# .. Biz bu uygulamızı sunucu üzerine koyup dışarıya(kullanıcılara servis) ediyoruz
# 4.Kök = İnternet ağ alt yapısı. Bunu dış dünyaya açabilmemiz için internet ağ altyapısı gerekli
# .. Bunu bir yerden internete entegre etmemiz gerekiyor
# Işte bunlar "turing.com" un servis edilebilmesi için gerekli IT altyapısı
# Cloud Computing bize bunları sağlıyor

# Biz bu altyapıyı nasıl oluşturabiliriz
    # 1. Klasik yöntem: Şirketin bodrum katını server odası(data center) yaparım. Internet bağlatırım. 
    # .. Network altyapısını tesis ederiz .İşletim sistemini kurarız sonra python kurarım, kameralarla güvenlik sağlarım,
    # .. elektrik gitmemesi için jenaratör bağlatırız, buna bir administrator ve veri tabanı yöneticisi veya DevOpsçu
    # .. dahil ederim ve vs vs onun üzerine de yazılımımı sunuculara yüklerim ve canlıya almış olurum. Ya da;
    # 2. Cloud computing: Yeni başlamış bir startup isem, minimum maliyetle işe gitmem lazım. Bunu buluttan alabilirim(Örn: AWS)
    # .. İş planıma göre cloud provider üzerinden alan adımı alırım sonra ayarları yaparım sonra cloud providerdaki işlemler
    # .. için bir devops elemanı işe alırım vs.
    # Cloud provider lar: AWS, Microsoft Azure, Google Cloud, Alibaba Cloud, Digital ocean ... vs

# Cloud computing nedir?
# Turing.com için gerekli olan ne varsa, internet üzerinde tutulan ve bir servis sağlayıcı tarafından verilen
# .. hizmetleri(Storage, Server, internet connection vs) sağlayan sistemler. Cloud provider ın sağladığı bu işlem
# .. cloud computing olmuş oluyor.
# "There is no cloud. It's just someone else's computer": Aslında bu aldığımız hizmet bir başkasının bilgisayarı/sunucusu
# .. Bunu bir cloud provider dan alıyorum.

# Bu nasıl ortaya çıktı
# AWS global çapta hizmet sunuyor. Bunun altyapısı çok güçlü. Gelen 100.000 lerce isteği amazon.com un 
# .. infrastructure ı gelen trafiği karşılayabiliyor. Black friday de bile.
# Bu milyonlarca isteği karşılayabilmesi için data center sistemleri var. Bu sistemler bazı dönemler boşta kalıyor
# Sonra bu sistemler boşta kalmasın diye Jeff Bezos , atıl kalan kapasiteyi başkalarına
# .. sunarak satayım diyor ve amazon bundan fayda sağlıyor
# Bizim bundan kazancımız var mı ? Bizim kazancımız şu: Bir server odası kurmak minimum(2 server ve yedekleri) 50.000 dolar
# Bunu kurdunuz diyelim. Belli bir süre sonra işi gelişince sunucu almanız gerekecek
# Bir sunucuyu alıp getirip kurmak, ihalesinin yapılması falan 1 aydan fazla süren bir şey. Ama AWS de böyle değil
# Amazonda 2 cpu lu 8 gb lık bir sunucu kullanıyorsanız bunları yükseltmek bir "tık"lık iş
# Eğer bunu kullanmayacağım derseniz satmak isterseniz bu da zaman alacak bir şey ama AWS de tekrar cpu ları gb kullanımlarını vs 
# .. düşürebiliyoruz anında. Ayrıca altyapının bakımını, güvenliğini vs vs de yapmak zorunda kalmıyoruz

# Cloud denince akla ne geliyor? Cloud çeşitleri neler?
# Genelde depolama ile alakalı olan şeyler. Google Drive, Icloud, Dropbox, OneDrive gibi. Burası buzdağının görünen yüzü
# .. Ancak cloud un daha farklı yönüde var --> Cloud Computing
# Cloud computing, bilgisayarın ram inin cpu sunun, network unun, grafik kartının, storage ının vs nin kullanılmasıyla
# .. ortaya çıkan şeye cloud computing ismini veriyoruz. Bu da buzdağının görünmeyen kısmı
# Data scientist olarak bizlede bu buzdağının görünmeyen tarafındayız
# Veriyi depolamak ile veriye bir değer katmıyoruz. Bunu hizmete sunmak için cloud computing ile kullanıcıların kullanımına
# .. sunarsam hemp bana, hem kullanıcılara faydası olur.

# Neden buna ihtiyaç duyuldu?
# "The sprit of the time"
# Taş devri neden bitti,  metallerin devri başladığı için taşın devri kapandı
# Neden elektrikli araba kullanıyoruz. Petrol tükeniyor, hava kirliliği, küresel ısınma gibi nedenlerden dolayı
# Sonuç olarak, zamanın ruhunu yakalamamız lazım.
# O yüzden bizde cloud computing e kayıtsız kalamayız. Günün birinde buna geçmek zorunda kalacağız
# Ev kullanıcı olarak bu hizmeti sağlayan cloud provider lar işte. Çünkü ev kullanıcısı olarak sadece 2 saat kullanacağım. 
# .. Sonra kullandığım kadar ödeme yaparım. Yoksa bu altyapıları kurmamız gerekir

# Peki bunun ardında yatan teknoloji ne ?
# 1.Virtualization
# Bizim bilgisayarımızda(Sunucumuzda) Hardware-Operating System-Hypervisor var
# Bunu tek bir makina olarak kullanabilirim ama virtualization ın teknolojisini
# .. bu sunucuya eklemem ile birlikte bu sunucuyu birden fazla sunucu olarak kullanabiliyorum
# .. Virtualization teknolojisiyle bu hardware i alt parçalara ayırıyorum
# .. ve kapasitesine göre 5-6 tane sunucu çıkartıyorum. Buna virtualization diyoruz.Bunu sağlayan virtualization teknolojisi.
# .. Hardware deki kaynakları gruplandırma denilen kavram çıktı ve virtualization ortaya çıktı
# 2.Containerization Technology :Burada da farklı işletim sistemleri ve farklı sunucular oluşturabiliyorum. 
# .. Bu da Containerization Technology. Yani bilgisayar içerisinde bilgisayar, server içerisinde server oluşturabiliyoruz
# 3.Software development Cycle : Üstte bahsetmiştik. Önce yazılım sistemlerinin belirlenmesi, daha sonra dökümantasyonu hazırlıyoruz
# .. safhalara bölüp(şuraya basınca şuraya gidecek, şunu basınca şunu yapacak vs vs), sonra product owner atıyoruz. 
# .. Developer team i yönetiyor. Developer team ler 15 günlük sprintler şeklinde bizim vermiş olduğumuz dökümantasyona göre
# .. developer team geliştirme yapıyor Sonra test ediliyor hatalar çıkıyor, onlar düzeltiliyor sonra teste giriyor en son 
# .. sonra canlıya alınıyor vs. Bu döngüye Buna software developer cyle deniyor
# 4.Serveless: Topraksız tarım. Yani amazon size bazı hizmetleri serversız olarak veriyor. Javada bir yazılım geliştirdimiz diyelim. 
# .. Bunu AWS ye yüklüyorsunuz. Sonra hiç bir şeye karışmıyorsunuz. Bütün o java ile yazılmış app in çalışması için olan
# .. gerekli her şeyi AWS sizin yerinize hallediyor. Böyle bir hizmette var

# Biz bu AWS nin sağladığı hizmetleri nasıl alıyoruz. Cloud provider lar bu hizmetleri hangi isimler altında sağlıyor buna bakalım
# SaaS : Software as a Service
    # Cloud provider dan bir yazılım olarak alıyoruz ve hiç bir şeye karışmıyoruz
    # Örneğin: Slack, Word, Excel vs. Yani bakımına, onarımına vs karışmadığınız kullandığınız programlar
    # Other Manages: Applications, Data, Runtime, Middleware, O/S, Virtualization, Servers, Storage, Networking
    # You Manage   : -
# PaaS : Platform as a Service
    # Cloud provider dan bir platform satın alıyoruz. Sadece Platform a ödeme yapıyoruz.
    # .. Sunucu dahil, sunucu üzerinde pyhton, java vs kurulu bir servis veriyor
    # Other Manages: Runtime, Middleware, O/S, Virtualization, Servers, Storage, Networking
    # You Manage   : Applications, Data
# IaaS : Infrastructure as a Service
    # Cloud provider dan bir alyapı olarak alabiliyoruz. Sadece makinayı satın alıyoruz
    # .. Bize makinayı/server ı veriyor. Server üzerinde gerekli işletim sistemi, uygulamalarımızı kuruyoruz ve bu servisi kullanabiliyoruz
    # Other Manages: Virtualization, Servers, Storage, Networking
    # You Manage   : Applications, Data, Runtime, Middleware, O/S
# On-Premises      :
    # Herşeyi kendimizin yaptığı(Str 50 de klasik yöntem diye bahsedilen)
    # Other Manages: -
    # You Manage   : Applications, Data, Runtime, Middleware, O/S, Virtualization, Servers, Storage, Networking

# Üsttekileri bir pizza analogy si ile anlatırsak. Bir pizza yiyeceksiniz
# SaaS        : Dominosa gidiyorsunuz. Pizzayı yiyip kalkıyorsunuz. Sadece hizmete para ödeyip çıkıyorsunuz
# PaaS        : Pizzayı eve söylüyorsunuz. İçeçeği ve masayı siz hazırlıyorsunuz
# IaaS        : Pizzayı dondurulmuş olarak alıp siz pişiriyorsunuz
# On-Premises : Pizzanın hamuru, malzemeleri dahil hepsini siz yapıyorsunuz

########## Şimdi AWS tarafına geçelim - Table of Contents
    # Introduction to AWS
    # What does AWS offer?
    # AWS Infrastructure
    # AWS Free Tier
    # Creating an AWS account

##### AWS(Amazon Web Services)
# Bu alanda piyasa lideri. Diğerleri bu concepti AWS den alıp kendi sistemlerini oluşturmuşlar
# Google çok benzer bir sistem oluşturmuş. Microsoft Azure biraz daha kullanıcı odaklı bir sistem geliştirmiş
# Production için AWS diğerlerine göre öne çıkıyor. Bundaki özellikler çok daha fazla

##### AWS bize ne sağlıyor. Bazı servislere bakalım
# EC2                    : Sunucu
# S3                     : Storage. Sitemizin(Turing.com ın) Images leri, ürünlerle ilgili bilgiler vs. 
# IAM                    : Hesabın güvenliği için kendi hesabımızda kullanıcı oluşturup(IAM diye) bunu yetkilendireceğiz
# CloudFormation         : Bazı şeyleri otomatize edebilmeniz için gerekli bir servis
# ElasticBeanstalk       : Siz kodu veriyorsunuz AWS sizin yerinize altyapıyı oluşturuyor
    # .. Ben bir şeyden anlamıyorum, kodu yazarım başka bir şeye de karışmam diyorsanız.
# Amazon RDS             : Veri tabanı hizmeti
# AWS Direct Connect     : AWS nin data center ına direk bağlantı yapabiliyorsunuz
# Amazon EBS             : Bilgisayarlardaki block storage
# Elastic Load Balancing : Gelen yükü dağıtma hizmeti
# Amazon Route 53        : Alan ismi alabiliyorsunuz
# Amazon VPC             : Kendinize özel VPC niz oluyor
# Elastic IP             : IP hizmeti alabiliyorsunuz
# AWS Snowball           : Çok büyük miktarda veriyi aktarmak için kullanılıyor. 
# .. AWS gönderiyor size siz veriyi aktarıp geri gönderiyorsunuz
# AWS Snowmobile         : Bu da veri aktarımı için kullanılıyor(Tır/Kamyon).
# 27 tane region, 87 availability zone u var. 226 servisi var AWS nin.Global olarak AWS nin büyüklüğüne erişen yok. 
# Compute anlamında 17, Veritabanı anlamında 11, ML alanında 32 hizmet vs vs
# Piyasada %34 lük payı var, Azure %21, Google Cloud %10, Alibab %5, IBM cloud %4, ...
# https://www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-infrastructure-service-providers/

##### AWS nin eksileri
# Karmaşık hizmetlerin işlevleri yeni başlayan kişiler için zor olabilir. Eleman almanız gerekebilir vs
# Faturalandırma karışık olabiliyor
# Diğer cloud provider lara göre daha pahalı

##### Bu servisleri nasıl kullanıyoruz
# Bir sitem/yazılımım var diyelim. Canlıya alacağız bunu # NOT: Canlıya almak: Sunucu üzerine koyup, kullanıcıların hizmetine açmak
# Canlıya alacağız diyelim. AWS yi de cloud provider olarak seçtik diyelim.
# Müşteriler sigh up yapacaklar, ürünleri inceleyecekler, alacaklarını sepete ekleyecekler vs
# .. Biz diyoruz ki bana bunun için bir "EC2" ver. Yani AWS üzerinde bizim kullandığımız virtual machineler/serverlar
# .. Sonra bu server üzerine bir apache server(ya da engineX server) kurduk diyelim. Bu da bir server yazılım
# .. Yazılımı canlıya alabilmem ve bunu kullanıcılara servis edebilmem için gerekli olan yazılım
# .. Sonra "AWS Route 53" servisini kullanarak bir alan adı aldım
# .. Sonra images ları, envanter bilgilerini de "S3" storage da topladım
# .. Sonra siteme kullanıcılar üye olacak, ürün bilgileri olacak Sonra "RDS" aldım
# .. "RDS" ve "EC2" yu sağlamak için AWS bana bir "VPC"(Özel bulut alanı( verdi. Bu alana "RDS" ve "EC2" yu yerleştirdim.
# .. Sonra diğer hizmetlerle gerekli ayarlamaları yaptım ve benim e-ticaret sitemi hizmete açtım.
# .. Kullanıcılar geliyorlar gidiyorlar ürün alıyorlar. Sonra bir "AWS lambda"(lambda fonksiyonu) tetikleniyor ve
# .. adamın aldığı ürün envanter listesinden düşülüyor. Kargo servisi tetikleniyor kargo servisine gidiyor vs falan
# .. derken iyi bir sistem kuruldu ve giderek büyüyoruz diyelim
# .. Sonra aldığım "EC2"(Sunucu) kaldıramadı işlemi. Sonra ram i ve cpu yu arttırdım ama yetmiyor diyelim
# .. Sonra dedim bir makina yetmiyor. Bunu 4 e çıkardık(EC2) .. Sonra bu gelen isteklerin 4 tane sunucu arasında dağıtılması lazım
# .. bunun için "load balancing" hizmeti de aldım AWS den
# .. Sonra vermiş olduğum hizmete ilgi büyüyor ve yılbaşında vs de trafik artıyor. Yani
# .. bazen 4 sunucuya ihtiyaç duyuyorum bazen 16 sunucuya. Ben bu trafiğin ne zaman bailayacağını da tahmin edemiyorum
# .. O yüzden bunun otomatik olarak gerektiğinde 16 sunucuya çıkarılması gerektiğinde tekrar 4 e düşürülmesi gerekiyor
# .. Bunu otomatize etmek için "Auto scaling" hizmeti alıyoruz.
# .. Sonra ben dünya çapında bir hizmet veriyorum ve 10.000 lerce ürünüm var
# .. Belli bir ürüne bakmak için farklı ülkelerdeki insanlar hep benim "EC2"(Sunucum) üzerine yük biniyor
# .. Bu yükü azaltabilir miyim? Mesela Amerika kıtasında olanlar oraya yakın bölgeden, Avrupaya yakın olanlar avrupaya yakın
# .. bölgedeki sunucudan hizmet alsın. Bunun için AWS den CloudFront(Cash) hizmeti aldık. Almanyadakiler mesela almanyadaki
# .. cash noktasından(sunucusundan) bu hizmeti alıyorlar vs vs. Hem sistemi hızlandırdım. Hem sunucunun yükünü azalttım
# .. hem de maliyeti azalttım. Burada tabi EC2 ve CloudFront hizmeti ücretli ama CloudFront daha uygun o yüzden onu da kullandık vs
# Burada AWS servislerinin nasıl kullanılabileceği ile ilgili örnek vermiş olduk

##### AWS Infrastructure
# En dışta AWS nin region ları var 27 tane. Region lar şehirler. 
# Onun altında availability zone lar. Region içerisinde en az 3 tane olacak şekilde availability zone var
# .. availability zone lar arasında fiberoptik kablolarla bağlantı var. Bir de güvenlik encript ediliyor(sağlanıyor)
# .. Yüklediğiniz veri 3 tane availability zone a kopyalanıyor. Bir zone da deprem vs olduğunda veri kaybını önlemek için 
# .. böyle bir sistem var.
# Availability zone altında da data centerlar(Binalar) var. Availability zone lar içinde data centerlar var
# Bir de local zone denilen kavram var. Bazı yerlerde region yok. AWS buraya mobile olarak mobil region gönderiyor
# .. Bu hizmey sadece Amerika kıtasına veriliyor

##### AWS Free Tier
# Free Tier kapsamında, Always free, 12 month free, free trials(2 aylık 3 aylık) gibi hizmetler var
# Bazı yaygınlaştırmaya çalıştığı hizmetler ücretsiz şu an(MongoDB)
# Sizin kullanacağınız "Amazon SageMaker"(ML ile alakalı) 2 ay ücretsiz. 2 aydan sonra ücretli hale geliyor
# Bu AWS free tier size servislere alıştırmak için bunları sağlıyor
# NOT: Bazı hizmetler free tier değil

##### Billing Policy
# 12 kullandıktan sonra ücretlendirme var mesela. Ya da aylık 750 saati doldurdunuz diyelim
# ..  Bu servisleri kullanırken billing alarmı olmadı. Mesela bazen EC2 yu kullanıyorsunuz sonra o orada 
# .. açık kalıyor. Bir uyarı gelmesi lazım.
# AWS hizmetleri ile ilgili bir hesap makinası(Create estimate) var. Buna basarak bir hesaplama yapabilirsiniz
# .. Bu hesaplamaları kaydedebilir "My Estimate" alanından görebiliriz

##### IAM Users
# Bir hesap açtınız e-mail adresinizi giriyorsunuz. Bu sizin root hesabınız. Biz root hesap
# .. kullanmayı tavsiye etmiyoruz güvenlik açısından. Root yetkileri kullanılacakssa "to do" komutu ile
# .. root yetkisi alınır kullanılır ve bırakılır
# Biz IAM Users oluşturacağız sonra hep IAM user ile gireceğiz.
# Güvenlik harici bir diğer sebepte bir hesapta birden kullanıcı çalışıyor. 
# .. Eğer root user ile girerse bir şey silerse bunu kimin yaptığını algılayamayız.
# AWS Management Console : Bizim size ayarladığımız kullanıcı hesapları AWS Management console u kullanmanızı sağlayacak.
# .. AWS login sayfasından rootuser ı seçerek giriş yapacağız sonra IAM user oluşturup onunla giriş yapacağız
# Programatic Access     : 
    # 1.Komut satrından : Bir de komut satırından bir erişim oluyor. Mesela console a("aws" console cmd değil bu)
# .. "aws s3 ls" yazarsak, bizim storage servisindeki bucketların listesini veriyor. Bucket: Simple storage 
# .. servisindeki klasör. 
# .. Hoca bir komut çalıştırdı uzun. Şu an console a bağlı değilim ve sunucuların listesini aldık. Bu aynı zamanda
# .. kaynak oluşumunu da sağlıyor. Yani komut satırından kaynak oluşturmanızı da sağlıyor. Bunun credential ları var
# .. Bunun "secret key" ve "access key" leri var. Bunları tanımlayarak bu şekilde sistem üzerinde uzaktan
# .. console a bağlı olmadan işlem yapabiliyoruz. Bu da "programatic access"
    # 2.SDKs: Bir de "programatic access" in SDKs olanı var. Diyelim ki Javada yazdığınız bir uygulama var
# .. bu uygulama gidecek S3 servisinde bir bucket(klasör) oluşturacak. Java programlamlama dili AWS nin programlama
# .. dilini biliyor mu bilmiyor. Araya bir tercüman gerekiyor. Bu tercüman SDKs. AWS API larının  anlayabileceği
# .. dile dönüştürüyor. Bu SDKs de yazmış olduğunuz programların içine gömülü bir paket.

# AWS key : Kesinlikle hiç bir yerde paylaşmıyoruz. Eğer görünürse silip yeni key oluşturacağız
# .. Bu olursa eğer consolunuza dahi girmeden biri hesabınızı kullanabilir.

# Hands-on a geçiş yapalım. IAM user açacağız ve biraz siteden bahsedeceğiz
# Buralar videodan izlenirse daha hızlı olur
# Notlar
# N.Virginia yı kullanacağız. AWS nin bütün servisleri burada var. 6 tane availability zone var
# IAM USER oluşturma
# 

#%% MLDP-2
# INTRODUCTION to EC2
    # Introduction to EC2
    # EC2 Instance Types
    # Creating an EC2 instance
    
# Bu gün AWS üzerinde sanal sunucu oluşturacağız(EC2) ve buna bağlanacağız.

##### What is EC2?
# EC2: Elastic Compute Cloud
# Amazondaki virtual machine EC2 olarak adlandırılıyor.
# EC2 instance, yani instance denilince AWS üzerinde bir sanal sunucuyu anlamalıyız
# EC2 instance üzerinde yazılımlarımızı çalıştırabiliriz. Java, .NET, C#, Python, ML algoritmalarının vs 
# .. çalıştırılmasını sağlayan sanal machine e EC2 instance diyoruz
# Ihtiyacımıza göre EC2 instance ı istediğimiz kapasitede(CPU, harddisk, network vs vs) AWS den alabiliyoruz.
# EC2 instance ın kullanım alanları : Ders sonunda web sunucu/servis üzerinden göstereceğiz. Orada bir web sayfası yayınlayacağız
# .. Bunun bir çok alanda kullanımı var. Veritabanı, web , ML ve bitcoin olarak kullanılıyor EC2 instance
# NOT: Virtualization technology si bir tane olan makinayı çoklamayı sağlıyordu

# AWS den aldığımız EC2 instance ın içerisinde neler var. Bunu local bilgisayarımızla karşılaştıralım
# Amazon Machine Image : Bizim local bilgisayarımızda  Mac, windows, ubuntu gibi bir operating system kurulu . 
# .. AWS den aldığımız EC2 instance ın içinde de bir yazılım var. Bu yazılım linux, windows, macos vs olabilir
# Bu yazılımı bize AWS bize bir "image"(kalıp) olarak sunuyor. Eskiden CD içerisinde windows 98 vardı yüklüyorduk
# .. Bunu bir CD olarak düşünebilirsiniz. İçinde bir işletim sistemi yüklü. Hatta içinde .NET , Java, Python image ı
# .. yüklü olarak dahi sunabiliyor.
# EBS Volumes    : Harddisk. Bizim SSD harddisklerden veya diğer türlü harddisklerden çok bir farkı yok. Fark olarak biz bunu
# .. bulut üzerinde kullanabiliyoruz
# Instance Type  : Instance ın CPU su, Ram i, gücü/kapasitesi.
# Security Group : Instance a bir güvenlik duvarı sağlıyor. Bu sunucuya gelen gidenleri kontrol eden mekanizma.
# .. Bizim izin verdiğimiz istekleri kabul ediyor, izin vermediğimiz istekleri reddediyor
# NOT: Sunucu data centerlarda data cabinetlerde bulunan ekransız bir şey. Ekran olarak kendi ekranımızı kullanıyoruz

##### EC2 Features
# Bu EC2 instance ı mesela ML işlemleri için 2-3 saat kullanıp kullandığınız kadar da ödeyeceksiniz
# AWS bu hizmeti bize 1 dakika içerisinde sunuyor
# Istediğimiz kapasitede alabiliyoruz
# Istediğiniz zaman kullanıp, istediğimiz zaman kapatabiliyoruz
# 1 saatten tutun 5 yıla kadar kendinize kaynak ayırabiliyorsunuz

# EC2 instance ı ayağa kaldırabilmek için;
# AWS console dan(Iam User oluşturduğumuz yer) kendimize bir EC2 instance ayağa kaldıracağız. Istediğimiz kadar kullanıp istediğimiz kadar 
# .. saf dışı da bırakabiliyoruz

# Ihtiyaca göre bir çok EC2 instance tipi var(557 tip)
# Yapacağınız iş CPU ağırlıklı bir iş ise CPU su yüksek bir EC2 instance alabilirsiniz. Network ağırlıklı ise network u yüksek vs alabilirsiniz
# Bu 557 tip i consol a girdiğimizde bunları instance type bölümünde görebiliyoruz
# https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#InstanceTypes:
# Burada CPU ya göre sıralayabiliriz, Memory ye göre sıralayabiliriz. Fiyatları da yanlarında görebiliriz   

##### EC2 instance tipleri
# Fiyata göre ve Amaca göre. NOT: AWS nin fiyata göre bir isimlerdirmesi yok normalde biz böyle adlandırdık
# 1.Pricing Model of Instance
    # On demand Instance : Bizim kullandığımız instance tipi. Hands-on(derste) da açıp sonra kapattığınız instance tipi
    # .. AWS ye hiç bir taahhütte bulunmuyorsunuz. Bunu günlük kullanımlarımız için kısa süreli işlem yapmamız 
    # .. gerekiyorsa bunu kullanıyoruz. Production için uygun ve ekonomik değil, hands-on ve development için daha uygun bu tip.
    # .. Bunun saatlik bir ücreti var(0.0116) .. Örneğin 30 dk lık bir kullanım yaptınız(0.0058) , 1 month(8.32)
    # .. Normal ücretlendirme saatlik ama saatin altında bir kullanım varsa da dakika ücretini ödüyorsunuz
    # Reserved Instance  : Bu sunucunu 1-2-3 vs yıl boyunca kiralayacağım diyoruz(%75 e kadar indirim var)
    # .. Makinayı değiştiremiyorsunuz. O yüzden dikkatli seçilmeli. Uzun süreli kullanım ihtiyacı varsa kullanıyoruz
    # Spot Instance      : AWS nin elinde o anda boş olan kaynaklarını kullanabiliyoruz. Çok uygun fiyatlar(%90 a kadar indirim)
    # .. Yalnız bunda fiyat belirliyorsunuz. O fiyatın üstüne çıkarsa makinanın fiyatı, o zaman AWS, EC2 instance ınızı kapatıyor 
    # .. Production ortamı için uygun değil. Testler ve kısa süreli analizler ve mining için kullanabilirsiniz
    # Dedicated Instance : Sunucunun birini bizzat veriyor size AWS. Reserved den farkı onda boşta hangisi varsa onu veriyor
    # .. O sunucu içinde bölünmüş bir bölümü kullanıyorsunuz reserved de. Dedicated de başka birisi onu kullanamıyor
    # .. Neden makinayı satın alıyoruz. Diyelim ki lisanslı bir yazılımınız var. O yazılımı bu makina üzerine kurduğunuzda
    # .. o makinanın bilgilerini alıyor ve lisanslıyor. Bu makinayı değiştirirseniz lisans geçersiz olur 
    # .. O yüzden yüksek miktarlı lisans ödediğiniz yazılımınız varsa. Bu lisansı sabit bir makinada kullanmanız lazım
    # .. ki lisans devamlı geçerli olsun.
    # Saving Plans       : Reserved instance gibi bir durum var. AWS ye diyorsunuz ki 5000 saat kullanım istiyorum vs 
    # .. diye bir taahhüt te uyguluyorsunuz.Yani bir nevi kontur satın alıyor gibi düşünebiliriz
    # NOT: Reserved ınstance, dedicated instance ve saving plans taahhütlü
    # Bunlar fiyata göre kategorilendirmeydi
# 2. Purpose Model
    # General Purpose   : T , M, A serisi
        # Genel amaca yönelik bir EC2 instance
    # Compute Optimized : C
        # CPU gerektiren işler için. Yüksek işlemcili bir şeye ihtiyaç duyuyorsak(Batch processing, media transcoding, gaming için vs)
    # Memory Optimized  : R,X,U,Z
        # Ram gerektiren işler için
        # Veritabanı kullanımları, gerçek zamanlı veri analizleri işleri için
    # Storage Optimized : D, I, H
        # Disk kapasitesiyle ilgili bir ihtiyacımız varsa
    # Accelerated Computing : F, P, G tipleri
        # ML için kullanılacak makinalar. Sizin işiniz burada

###### EC2 instance isimlendirmesi
    # Purpose    : Amaç
    # Generation : Jenerasyon.. 3. jenerasyon, 4. jenerasyon gibi
    # Dimension  : Boyut. Makinamızın memory ve CPU olarak büyüklüğünü ifade ediyor

###### Billing Alarm    
# Billing alarm kuracağız. Bunu IAM user ile kurabilirsiniz ancak sorun olmaması için root hesaptan yapacağız
# Root hesapla girip arama yerine "cloudwatch" yazıp tıklıyoruz --> (solda) --> alarms -- billing
# .. --> Create alarm --> (6 saatte bir kontrol yapacak) --> (Değişecek yerler)--> Whenever EstimatedCharges is... --> Greater/Equal
# .. --> Alta "4" USD giriyoruz
# .. --> Next --> (Değişecek yerler) --> "Create new topic" seçilecek --> (Onun altına Create a new topic… kısmına) --> "Billing_Alarms_Topic" yazalım
# .. --> (Email endpoints that will receive the notification… kısmına) --> mail adresinisi yazın --> "Create topic" diyelim
# .. --> (Mailden confirmation a basın) --> 
# .. --> (Basınca(Mail confirmationdan önce) Select an existing SNS topic kısmına döndü) --> Altta "Billing_Alarms_Topic" i seçelim --> 
# .. --> Next --> Alarm name: Billing Alarm --> Next --> Create alarm dedik
# Buradan çıkalım şimdi log out diyelim. 

# Iam User ile giriş yapalım
# N.Virginia yı seçelim sağ üstten(Seçili değilse)
# EC2 instance oluşturacağız
# Arama yerine EC2 yazalım ve "EC2" ya girelim --> Solda "instances" da --> "Instances" a tıklayalım --> 
# .. --> sağ üstte turuncu "launch instance" a tıklayalım. Sanal sunucu oluşturma bölümü burası
# .. Name den isim verebilirim "My ML Server" diyebiliriz mesela ---> 
# .. (add additional tags) e basarsak --> (add tag) --> (Key --> Env) ve (Value -->DEV) şeklindede yazabiliriz
# .. ancak şimdilik bunları yazmadık sadece "My ML Server" dedik ve geçtik
# .. Bu bölümün altında "Application and OS Images(Amazon Machine Image)"(AMI) kısmı var.
# .. AMI: Şablon demekti. Işletim sistemimizi barındıran kalıp/image/şablon(CD örneği vermiştik).
# .. İşletim sistemi bu image ın içinde kurulu. Böyle kalıp halinde bir operating sistem(ve belki bir de apllication) şablonu veriyor
# .. Burada "Amazon Linux", amazonun kendi üretmiş olduğu bir linux var. Bunu santos işletim sisteminde değişiklikler yaparak üretmiş
# .. Bunu çalıştırabiliriz, ubuntu, windows vs kullanabiliriz. Çeşitli firmaların AMI ları var(Quick start kısmında)
# .. Bizim kullanacağımız "Amazon Linux" ya da "ubuntu" olur. Bu image larında çeşitleri var free tier olanı var olmayanı var
# .. Description ın üstündeki yere tıklarsak "Amazan Linux" un çeşitlerini görebiliriz. 
# .. En stabil sürüm genelde en sondan bir önceki sürüm olur. Bizde onu seçeceğiz. Yani Kernel "4.14" yazan. Onu seçelim
# .. Bir de burada browse AMI lara tıklarsam AWS üzerinde bulunan bütün AMI ları gösteriyor. 
# .. Sadece free tier olanları filtreleyebiliyoruz istersek
# .. "My AMI" bölümünde, kendi oluşturduğumuz AMI lar var.
# .. "AWS Marketplace AMIs" da bazı firmalar kendi image larını üretip satıyorlar
# .. "Community AMIS" da genelde community ye sunulan ücretsiz AMI lar oluyor
# .. Biz burada "Quick start" ı kullanacağız. Decriptiondan X86 veya arm seçimi yapabiliriz
# Instance type --> Bizim genelde kullanacağımız type t2 micro, eğer bu yoksa t3 micro yu kullanabilirsiniz(Bunlar ücretsiz)
# Key Pair --> create new key pair --> (key pair name) --> "my-key" --> (key pair type) --> RSA --> (private key file format() --> .pem
# .. ---> create key pair diyoruz. Key pair imizi indirilenler klasörüne indirdi

# 2. session ın 3. dersi yok. (EC2 oluşturma. Bu süreç MLDP-4- Streamlit-2 notundan da öğrenilebilir)

#%% MLDP-3 Streamlit-1
# Model deployment yapacağız
# Önce "virtual environment" oluşturacağız. (Ne olduğundan altta bahsedeceğiz)
# Virtual environment oluşturmak için "Git Bash" kullanacağız(Windows kullananların). 
# .. Mac i olanlar(mac in terminalini kullanabilirler) .. Visual studio da kullanılabilir ancak hatalar 
# .. olabiliyor çok. Anaconda prompt tada kodlar farklılık gösteriyor biraz

##### Virtual Environment
# Environment ı neden kullanıyoruz. Farklı projelerde farklı sürümlere ihtiyacımız olabilir.
# .. Bu yüzden virtual environment lar oluşturuyoruz(Kütüphane sürümü: pandas 1.2.1, pandas 1.2.2 .... gibi)
# Altta environment oluşturma şekillerini göreceğiz sonra 

##### Anaconda ile virtual environment oluşturma
# Anacondayı açınca sol üstte "Home" kısmında "Applications on" var. Orada environment lar görünüyor
# Farklı bir environment seçersek orada anaconda sayfası değişecek ve o environment active olmuş olacak. 
# Birazdan environment oluşturup bu environment ı active edeceğiz. Yeni kütüphane yüklediğimizde
# .. yeni oluşturduğumuz environment üzerinde o yüklediğimiz sürümler indirilecek.
# Peki environment nasıl oluşturacağız? Bunu kod ile active etmeyi göstereceğiz
# Eğer anaconda da bunu yapmak istersek solda "Environments" kısmı seçili olduğunda altta "create" 
# .. butonu var. Orada tıklayarak yeni environment oluşturabiliriz. (Not: Anaconda da "Anaconda prompt" ile yapmak mümkün)

##### Visual Studio Code ile environment oluşturma
# Visual studio da bir tane python dosyası açıyoruz
# Sağ üst köşede environmentları seçebiliyoruz
# Sonra üstte arama yerine tıkladığımızda seçtiğimiz environment ı görebiliriz.
# .. Bu arama bölümünde projelerimizin yanında projelerimizin hangi environment da olduğunu da görebiliriz.   

##### Streamlit
# 1. Create a folder on Desktop named "streamlit" and create a file named "my_app.py" inside it.
    # Masaüstüne streamlit klasörü oluşturalım ve hocanın attığı dosyaları içine atalım
# 2. Create virtual environment
    # Bu adımda sorun yaşanırsa "python bulunamadı" diye. 3. adımdaki çözüme bakılabilir
    # a. method 1: from terminal --> python -m venv env_name  
      # Oluşturduğumuz klasörün üzerine sağ tık --> "Git Bash Here" a tıklayalım --> "ls" yazalım -->
      # .. --> (Klasörün içindeki dosyaları ve environment ı görüyoruz) --> "python -m venv my_environment" yazalım
    # b. method 2 : from anaconda --> create environment (by mouse)
      # Anacondadan yukarıda anlatılan şekilde "create" ile yapılabilir 
# 3. activate venv (you can skip this step if you use anaconda)
    # source env_name/Scripts/activate  # (if not works try without source) 
        # Üstteki kodu yazıyoruz. Çalışmazsa "source" yazmadan deniyoruz. Yine çalışmazsa slash ları ters çevirip yazıyoruz
        # .. Yine çalışmazsa aşağıdaki kodları deneyebiliriz
            # pip install --upgrade virtualenv
            # virtualenv -p python3 env_name 
            # .. Sonra tekrar alttaki
            # source env_name/Scripts/activate           
    # (in linux/mac machines "bin" instead of Scripts: see below) 
       # source env_name/bin/activate 
    # (python.exe -m pip install --upgrade pip) if required
    # (just "deactivate" to deactivate the venv)
    # (if you want to create conda env: see below)
       # open anaconda promter
       # conda create -n env_name
       # conda env list
       # activate env_name
       # conda deactivate
# 4. add packages into venv
   # a. method 1: 
      # pip install streamlit
      # pip install sklearn
   # b. method 2:(if you already have requirement file)
      # pip install -r requirements.txt
      # NOT: Bir paket diğerleri olmadan
      # Bizde requirements.txt dosyası vardı bunu kullandık. Dosyanın alttakiler yazıyor
          # scikit-learn==1.10.2
          # streamlit==1.10.0
          # pip list  -->  to see the packages
          # pip freeze > requirements.txt -->  to create requirement file"""
  # Note:
      # (python -V)
      # (streamlit version)
# 5. streamlit run my_app.py
    # Bunu yazınca bir site açılacak browser da otomatik

# Daha sonra my_app.py dosyasını açıyoruz(Biz spyder da açtık)
# Oraya alttaki komutlar yazıldıkça ve kaydedildikçe browser da açılan yerde değişiklikler olacak
# Yani komutu yazıyoruz spyder da sonra "save" e basıyoruz daha sonra browser da açılan sayfaya gidiyoruz
# .. sağ üstte "Always Rerun" seçeneğini buluyoruz. Basınca python da yapıtıklarımız bu sitede görünecek
# Sonuç olarak biz python da her bir şey yapıp(kod yazıp) "save" edince sitede o kodların çıktıları
# (always rerun) dersek önümüze gelecek.

###########################################################################################
# BIZIM KODLAR(Hepsi aynı hocayla ama kaçırılan yer vardır belki diye altta Hocanın kodları da var)
"""
#!pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
# import sklearn

st.title("This is a title")

st.text('This is some text.')
st.markdown("Streamlit is **_really_ cool** :+1:")
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.header('This is a header')
st.subheader('This is a subheader')

st.success('This is a success message!')
st.info('This is a purely informational message')
st.error('This is an error')

st.write('Hello, *World!* :sunglasses:')

# image ekleme

img = Image.open('images.jpeg')
st.image(img, caption="cattie") # ölçeklendirmesini otomatik yaptı
# st.image(imf,caption="cattie", width=300)

# video oynatma -- bunu youtube videosu falan da oynatabiliyorsunuz
# my_video = open("ml.mov,'rb') 
# st.video(my_video)
st.video("https://www.youtube.com/watch?v=EWNE3PywXwk")

cbox = st.checkbox("Hide and Seek") # tik atıyorsunuz ama bunu bir şeye bağlayabiliriz

if cbox:
    st.write("Hide")
else:
    st.write("Seek")
    
# radio button
# st.radio("Select a color",("blue","orange","yellow"))    

status = st.radio("Select a color",("blue","orange","yellow"))
st.write(status)  # if kullanmadan kısa yöntem
    
# button
st.button("Button") # Veriler girilir. En son tuş konulur(button). Yani predict tuşu
if st.button("Press me"):
    st.success("Analyze Results are...")    
    
# Select box
occupation=st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor"])   
st.write(occupation)
    
#multi_select
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])

#slider # Bu önemli
option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5) # min ve max ı yazmak zorunda değilsiniz
option2 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=5.2, step=0.2)
# Not: integer ise yazacağın değerlerin hepsi int olmalı. Float için aynı mantık
result = option1 * option2    
st.write("multiplication of two option is:",result)

#text_input
name = st.text_input("Enter your name", placeholder="Your name here")
if st.button("Submit"):
    st.write("Hello {}".format(name.title()))
    
#code
st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np") 

with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df

#date input
import datetime
today=st.date_input("Today is", datetime.datetime.now())

#time input
the_time=st.time_input("The time is", datetime.time(8,45))

#sidebar
st.sidebar.title("Sidebar title")
st.sidebar.header("Sidebar header")

a=st.sidebar.slider("input",0,5,2,1) # Soldan(sidebardan bilgileri aldık ...)
x=st.sidebar.slider("input2")
st.write("# sidebar input result")
st.success(a*x)  # Sağa yazdırdık

# Dataframe # Burası önemli
# 3 adet yöntem var df okutmak için
# st.table(df.head())  
# st.write(df.head()) #dynamic, you can sort
df = pd.read_csv("Advertising.csv", nrows=(100))
st.dataframe(df.head())#dynamic, you can sort 
st.write("#")

# My_model bizim kaydedilmiş ML algoritması
# modeli kurduk, eğittik, dump ile kaydetti
# 3 değer giriyoruz(tv,newspaper,radio) sales i tahmin ediyor # r2= 0.86
# !pip install sklearn
# import sklearn
import pickle
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))

TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)

my_dict = {"a":[1,2,3,4],"b":[4,5,6,7],"c":[9,10,11,12]}
df=pd.DataFrame(my_dict)
st.table(df)

#Predict
if st.button("Predict"):
    pred = model.predict(df)
    st.write(pred[0])

# html
html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Single Customer </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
"""

############################################################################################
# HOCANIN KODLARI
"""
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
​
​
st.title("This is a title")
st.text('This is some text.')
st.markdown("Streamlit is **_really_ cool** :+1:")
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.header('This is a header')
st.subheader('This is a subheader')
​
st.success('This is a success message!')
st.info('This is a purely informational message')
st.error('This is an error')
​
st.help(range)
​
st.write('Hello, *World!* :sunglasses:')
​
#image
img = Image.open("images.jpeg")
st.image(img,caption="cattie")
st.image(img,caption="cattie",width=300)
​
#my_video = open("ml.mov",'rb')
#st.video(my_video)
​
#st.video("https://www.youtube.com/watch?v=uHKfrz65KSU")
​
#Checkbox
​
cbox = st.checkbox("Hide and Seek")
​
if cbox:
    st.write("Hide")
else:
    st.write("Seek")
​
​
# radio button
status = st.radio("Select a color",("blue","orange","yellow"))  
st.write("Your favourite color is", status)
​
#button
st.button("Button")
​
if st.button("Press me"):
    st.success("Analyze Results are...")
​
#select box
occupation=st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor"])
st.write("You selected this option:", occupation)
​
#multi_select
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])
​
#slider
option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)
option2 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=5.2, step=0.2)
result=option1*option2
st.write("multiplication of two options is:",result)
​
#text_input
name = st.text_input("Enter your name", placeholder="Your name here")
if st.button("Submit"):
    st.write("Hello", name.title())
​
​
#code
st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np")
​
​
with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df
​
​
#date input
import datetime
today=st.date_input("Today is")
​
#time input
the_time=st.time_input("The time is")
​
​
#sidebar
st.sidebar.title("Sidebar title")
st.sidebar.header("Sidebar header")
​
a=st.sidebar.slider("input",0,5,2,1)
x=st.sidebar.slider("input2")
st.write("# sidebar input result")
st.success(a*x)
​
# dataframe
st.write("# dataframes")
df = pd.read_csv("Advertising.csv", nrows=(100))
st.table(df.head())  
st.write(df.head()) #dynamic, you can sort
st.dataframe(df.head())#dynamic, you can sort
​
import pickle
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))
​
TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)
​
my_dict = {
    "TV": TV,
    "radio": radio,
    "newspaper": newspaper,
}
​
df=pd.DataFrame.from_dict([my_dict])
st.table(df)
​
if st.button("Predict"): 
    pred = model.predict(df)
    st.write(pred[0])
    
    
html_temp = """
#<div style="background-color:tomato;padding:1.5px">
#<h1 style="color:white;text-align:center;">Single Customer </h1>
#</div><br>"""
#st.markdown(html_temp,unsafe_allow_html=True)

#%% MLDP-4 Streamlit-2
# EC2 ya bağlanacağız. Detaylar aşağıda belirtilecek
# Dosyaları EC2 ya çekmenin bir kaç yöntemi var. Biz bunları "git" den clone edeceğiz
# Yöntemler için altta 10. maddenin a-b-c sine bakılabilir.
# .. c maddesinde; makinenizi sanal makinaya tanıtıp bir köprü oluşturup, buradan secure copy(scp) ile yapıştırabiliyorsunuz

# 1.Push the following files to the github 
    # -saved model
    # -app.py file (streamlit commands)
    # -requirements.txt and other files
# Masaüstündeki dosyaları github ınıza push etmeniz gerekiyor normalde ilk adımda ama hocanın hesabını
# .. kullanarak devam edeceğiz yapmaya. https://github.com/richardclarusway/inclass_streamlit.git
# 2. open your aws console
    #  AWS ye giriyoruz "IAM USER" ile (IAM USER detayları MLDP-1-2 dosyasında var)
# 3. Open EC2 Dashboard and Launch Instance (t2.micro )
    # EC2 ya giriyoruz --> Instances --> Instances --> (Sağ üstte turuncu) Launch Instances
    # --> (Name)                            --> "isim_girelim_buraya"
    # --> (Application and OS Images)(AMI)) --> aws linux machine
    # --> (Instance Type)                   --> t2.micro (Free tier eligible)
    # --> (Key pair login)                  --> create a new key pair --> (key pair name) --> "Johnson2" -->
    # .. --> default settings(RSA and .pem) --> create key pair e tıklıyoruz --> Dosya indi(.pem dosyası)
    # (En alta gelip sağ altta) --> "Launch Instance"(Turuncu) a tıklıyoruz
    
    # EC2 oluştu(Success yazıyor) --> Üstte "Instances"(Mavi) a tıklıyoruz tekrardan --> refresh yapalım
    # Oluşturduğumuz instance ı buluyoruz --> "Station check" , "2/2 checks passed" ve "Instance state", "running"
    # .. olana kadar bekliyoruz arada refresh yapabiliriz
    # .. NOT: Eğer hala çalışmadıysa üstten Instance state kısmında "Start Instance" a basabiliriz
    # Sonra oluşturduğumuz instance ın solundaki boş kutucuğa tıklıyoruz(seçelim). Altta bi şeyler belirdi    
    # "Security" ye tıklıyoruz(NOT: Normalde alttaki adımı instance oluştururken de yapabilirdik ama biz burada yapacağız)
# 4. Security Group Settings 
    # "Security groups" kısmında link gibi olan yere tıklayalım(sg-089cc47...... diye başlayan yer)
    # Sağ da "edit inbound rules" a tıklayalım
    # Add rule a 2 kere basalım 2 tane kural ekleyeceğiz
# 5. Due to we want our app to be public we should set following configurations:
    # a. Rule-1: Select "Custom TCP Rule" and set 8501 as port range and 0000 in soruce column (Anywhere IPv4) (8501 ve anywhere IPv4 kısımları yeterli)
    # b. Rule-2: Select "Custom TCP Rule" and set 8502 as port range and 0000 in soruce column (Anywhere IPv4) (8502 ve anywhere IPv4 kısımları yeterli)
    # NOT: source kısmını "custom" yaparsak herkes göremez.
    # Neden 8501 ve 8502 yazdık? Streamlit böyle seçmiş. Benim portlarım 8501 e baksın demiş. Boş ise 8501 e bakacak
    # .. boş değil 8502 ye bakacak
    # Toplam 3 tane rule umuz oldu((starting with SSH)). Sağ alttan --> "save rules" a tıklayalım
    # Şu an linkimi public yaptım. Birine link atınca onu görebilir. Custom yapsaydık göremeyecekti müşteri
    # Tekrar EC2 ya basıyoruz üstten geçiyoruz. -->"Instances" --> "Instances"
# 6. Connect to instance
   # Az önce inen .pem uzantılı dosyayı başka bir klasöre alabiliriz ya da download klasöründe de durabilir
   # .. .pem uzantılı dosyanın bulunduğu klasöre --> sağ tık 
   # .. --> git bash here(anaconda prompt ile yapacaklar "cd" ile o klasöre gitmeleri gerek)
   # Sonra AWS kısmına gelelim. Instance ımızın yanındaki boş kutucuğa tıklayalım(seçelim). Üstte "Connect" kısmına tıklayalım
   # .. (Gelen yerde) --> SSH client --> (Altta example kısmında .pem uzantılı dosyanızı kapsayan örnek hazır duruyor)
   # .. (Bunu kopyalayalım(NOT: @ den sonrası sizin public IP niz)) 
   # Tekrar git bash kısmına gelelim buraya yapıştıralım --> "enter" --> "yes" --> "enter" . Bağlantıyı kurduk
   # NOT: Eğer koparsa bağlantı git bash i kapatıp sonra .pem dosyasının olduğu dosyaya sağ tık --> "git bash here"
   # .. --> Tekrar linki kopyalayınca bağlanacağız. Tekrar "yes" yapmaya çalışırsak bir şey olmaz bu sefer direk bağlanır 
   # NOT:(47. dk) Burada hata alanlar git bash i açtığınızda bağlanmadan önce "chmod 400 yourpemname.pem" --> "enter" yapmalı
   # ... ya da kopyalanan koddan önce "sudo" yazıp sonra kopyalasınlar.
   # NOT: "chmod 400 yourpemname.pem" kodu pem file ın izin seviyesini düşürüyor(Yazılabilirden, okunabilir e düşüyor)
# 7. to see the python versions on your ec2 # 2.ders başı(1:13:50)s
    # Bunun içerisinde python yüklü. Python a bağlanmak için ;
    # "python" --> "enter" --> (Python a bağlandık) --> print("Hello") 
        # NOT:"python3" yazarsak python ın başka versiyonu gözükebilir(Python 3.7.1 gibi)
        # .. Eğer python3 olmasaydı --> "sudo yum install python3.7" --> "enter" yapınca yükleyecekti 3.7 versiyonunu
    # Python dan çıkmak için ;
    # --> "exit()" --> "enter" --> (Şimdi tekrar EC2 nun home page indeyiz)
# 8. to update python: 
    # Bu adımı yapmasak da olur ama yapalım
    # "sudo yum update -y" 
# 9. install git to ec2
    # Dosyaları EC2 ya "git" ile indireceğiz o yüzden "git" i install etmemiz gerekiyor
    # .. Yani EC2 nun içerisine "git" i yüklüyoruz
    # "sudo yum install git" --> "y" --> ("Complete" göreceğiz)
# 10. Copy app files into ec2
    # a. method 1 : use git clone method:
        # Şimdi eğer bizim github ımızda olsaydı dosyalar . Github da dosyaların olduğu yere girince
        # .. sağ üstte --> "Code"(yeşil) kısmından --> HTTPS linkini kopyalayacaktık ama hoca attı bunu bize(Altta)
        # .. "git clone" yazdıkdan sonra bu kodu yapıştıralım. (NOT: Bu kod "public" olmalı)
        # "git clone https://github.com/richardclarusway/inclass_streamlit.git" --> "enter" .--> (git den indirdik şu an)
        # "ls" yazalım --> "enter" --> inclass_streamlit klasörü geldi dizinimize
    # b. Method 2: if you are using vs code:
        # - Create folder in ec2 ("mkdir foldername" from terminal) 
        # - change directory to new folder
        # cd foldername
        # - Copy files from desktop into new folder
        # (rm -rf folder_name    --- to delete the folder with the files inside it)
    # c. method 3: 
        # if you cannot copy via vscode use secure copy method: 
        # scp -i richard_new_3.pem requirements.txt ec2-user@52.71.254.30:/home/ec2-user/streamlit6             
        # (your keypair should at the same the directory with target data)
        # Bunu uygulamak için .pem file ile requirements.txt aynı dosyada olmalı
# 11. cd to folder downloaded from github (cd: change directory)
    # "cd inclass_streamlit/" --> "enter" --> (Bunun içine girdik). Içinde ne var bakalım
    # "ls" --> "enter" 
# 12. Create venv 
    # Environment oluşturalım
    # "python3 -m venv env_name"
# 13. activate venv (maybe pip required -----python -m pip3 install -U pip3-------)
    # Environment i active edelim
    # "source env_name/bin/activate" --> (Bu olmuyorsa aşağıdaki denenebilir)
    # "source env_name/Script/activate" --> 
# 14. install required packages inside this folder s(foldername) in ec2
    # pip ile environment ı kuralım
        # "pip3 install -r requirements.txt" --> (Scikit-learn ve streamlit i kuracak)
    # or to install manually
        # - pip3 install scikit-learn==1.0.2st 
        # or (sudo python3.7 -m pip3 install scikit-learn==1.0.2)
        # - pip3 install streamlit==1.10.0  
        # or (sudo python3.7 -m pip install streamlit==1.10.0)
        # (pip3 list) to see the packages
        # (pip3 freeze > requirements.txt) to create requirement file
# 15. streamlit run my_app.py
    # Streamlit i başlatalım.
    # You can now view your Streamlit app in your browser.
        # Network URL: http://172.31.28.28:8501
        # External URL: http://18.188.133.122:8501
    # External linkini kopyalayalım(Mouse ile. Eğer "Control C" yaparsak çalışmayı durdurur(bkz: Adım 16))
    # .. Bu linki browser a yapıştıralım. Bu link "public" artık. Herkes girip görebilir.
    # NOT: Git bash i kapatırsanız streamlit çalışmayı durdurur(instance çalışıyor olsa bile)(Hocada durdurmadı ama normalde
    # .. kapanıyormuş).. Bunu önlemek için yani git bash i kapattığınızda da çalışması için tmux ı install edeceğiz
    # Şimdi çıkalım(Adım 16)
# 16. "Control C" to stop running app
    # Control c ile durdukduk. Şimdi "git bash" i kapatıp tekrar .pem dosyasının bulunduğu klasörden açalım "git bash" i
    # Yine bağlanalım --> satır 49-50-51 deki linki kopyalayıp  --> "enter"
    # "cd inclass_streamlit/" --> "enter" --> "ls" --> "enter" 
    # .. --> "source env_name/bin/activate" --> (Mac için) ("source env_name/Script/activate" --> (Windows için))
    # .. --> (şu an environment ımız aktif tekrar)
# 17. install the tmux
    # "sudo yum install tmux" --> "enter" --> "y" --> (Complete göreceğiz)
# 18. create a new tmux session
    # Yeni bir tmux session oluşturalım
    # "tmux new -s st_instance"  # Buradaki "st_instance" ifadesini değiştirebilirsiniz
    # tmux session içerisine girdik şimdi
# 19. run the app 
    # Şimdi tmux ın içinde streamlit i çalıştıralım
    # "streamlit run app.py"
    # Then it is ok. Even if you close the gitbash or what ever you are using for linux, the app will continue to work.
    # You can now view your Streamlit app in your browser.                                                                                     
        # Network URL: http://172.31.21.107:8501                                        
        # External URL: http://3.17.161.155:8501  # Hocada bunlar 8502 çünkü hocada 8501 kapanmadı açık kaldı
        # Bu linkten bağlanırsak tmux dan bağlanmış oluyoruz
    # Hocayı tmux dan attı. Tekrar oluşturulmuş tmux a bağlanmak için adım 20 de "tmux attach -t st_instance"
# 20. to detach from tmux session     # 3. ders başı
    # "tmux attach -t st_instance" --> (bundan sonra tekrar "streamlit run app.py" diyip bağlanmayı deneyebiliriz)
    # "control c" ile streamlit i durduralım ama hala tmux ın içindeyiz. Nasıl çıkacağız peki?
    # "control b" ye basalım. Sonra elimizi kaldırıp  "d" ye basalım(detach olduk. Alttaki yeşil ekran gitti. tmux dan çıktık)
    # Tekrar girmek istersek;(Yukarda bahsettik ama bir kaç kere yaptık bunu)
        # "tmux attach -t st_instance"
# 21. to kill the session
    # tmux session ı silmek istiyorsak;
    # "tmux kill-session -t st_instance"

##############################################################################
# Proje çözümü için ;
# Bir veri seti var elinizde
# Bu veri seti üzerinden feature selection yapacaksınız
# Hoca nın kodları
"""
new_list = ["age", "hp_kW", "km", "Gearing_Type", "make_model"]
X = df[new_list]
y = df['price']
X = pd.get_dummies(X)
X.sample(5)   # all numeric
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
from sklearn.ensemble import RandomForestRegressor
rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)
eval_metrics(y_test, y_pred) # R2 : 0.92 , rmse: 1997.45
import pickle
pickle.dump(rf_model, open('rf_model_new','wb')) 
###### Bundan sonrası aşağısı streamlit komutları ile yapılmalı 

richard_model = pickle.load(open('rf_model_new','rb')) # Bir tane model import edeceksiniz streamlit te
columns = list(X.columns)            # Feature lara bakacaksınız sonra
columns
my_dict = {"age":2,"hp_kW": 105, "km":100000, "Gearing_Type":"Automatic", "make_model": "Audi_A3"}
df = pd.DataFrame.from_dict([my_dict])
df.head()
df = pd.get_dummies(df)
df
df= pd.get_dummies(df).reindex(columns=columns, fill_value=0)
df.head()
prediction = richard_model.predict(df)
print(prediction)
print("The estimated price of your car is €{}. ".format(int(prediction[0])))
"""

####################################################
# Hoca: Eskiden yaptığım bir şeyi göstereyim dedi
# Churn prediction ın demosunu yapmışlar
# Müşteri belli değerleri girdiğinde 3 şey gösteriyor
    # 1.Churn probability of randomly selected customers
    # 2.Top Customers to Churn
    # 3.Top Loyal Customers


#%% MLDP-5-6-7-8 
# Buranın notları yok.

