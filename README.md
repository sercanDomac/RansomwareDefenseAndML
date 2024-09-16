RansomwareDefenseAndML projesi, sistem güvenliğini artırmak ve ransomware gibi siber tehditlere karşı etkili bir savunma sağlamak için geliştirilmiş bir çerçevedir. Bu proje, makine öğrenimi tabanlı anomali tespiti, dinamik IP bloklama, otomatik yedekleme ve şifreleme, immutable (değiştirilemez) yedekleme ve saldırı tespitinde otomatik uyarı ve müdahale gibi temel güvenlik stratejilerini içerir.

Proje İçeriği
1. Makine Öğrenimi Tabanlı Anomali Tespiti 🧠
Amaç: Ağ trafiğinde anomali tespiti yaparak olası siber saldırıları erken aşamada belirlemek.
Kullanılan Teknolojiler: Isolation Forest algoritması, scikit-learn.
Açıklama: Bu bölüm, ağ trafiği verilerini analiz ederek normalden sapmaları tespit eder ve potansiyel tehditleri işaretler.

2. Dinamik IP Bloklama ve Firewall Entegrasyonu 🔒
Amaç: Kötü niyetli IP adreslerini dinamik olarak engellemek ve firewall kuralları ile sistemi korumak.
Kullanılan Teknolojiler: iptables (Linux), firewall yönetim araçları.
Açıklama: Bu bölüm, tespit edilen kötü niyetli IP'leri engeller ve yetkisiz erişimleri önler.

3. Otomatik Yedekleme ve Şifreleme 🔐
Amaç: Verilerinizi otomatik olarak yedeklemek ve AES-256 ile güçlü bir şekilde şifrelemek.
Kullanılan Teknolojiler: Python cryptography kütüphanesi.
Açıklama: Yedekleme verilerinizi şifreleyerek ransomware saldırılarına karşı koruma sağlar.

4. Immutable (Değiştirilemez) Yedekleme ☁️
Amaç: Yedeklerinizi değiştirilemez hale getirerek ransomware saldırılarına karşı koruma sağlamak.
Kullanılan Teknolojiler: AWS S3 Object Lock.
Açıklama: Bulut tabanlı yedekleme çözümleri kullanarak yedeklerinizi değiştirilemez hale getirir.

5. Saldırı Tespitinde Otomatik Uyarı ve Müdahale 📧
Amaç: Saldırı tespit edildiğinde anında e-posta uyarıları göndermek ve otomatik olarak IP engellemeleri yapmak.
Kullanılan Teknolojiler: Python, e-posta gönderim hizmetleri.
Açıklama: Saldırılara hızlı bir şekilde yanıt vermek için otomatik uyarı ve müdahale mekanizmaları içerir.
Kurulum
Gereksinimler:

Python 3.x
Gerekli Python kütüphaneleri (scikit-learn, cryptography, boto3, vb.)
AWS hesabı (Immutable yedekleme için)
Adımlar:

Python kütüphanelerini yükleyin:
bash
pip install -r requirements.txt
Konfigürasyon dosyalarını düzenleyin (config.yaml, vb.).
İlgili Python scriptlerini çalıştırarak modülleri test edin.

Kullanım

Anomali Tespiti: anomaly_detection.py dosyasını kullanarak ağ trafiğinde anomali tespiti yapın.

IP Bloklama: dynamic_ip_blocking.py dosyası ile kötü niyetli IP'leri engelleyin.

Yedekleme ve Şifreleme: backup_and_encryption.py dosyası ile otomatik yedekleme ve şifreleme işlemlerini gerçekleştirin.

Immutable Yedekleme: AWS S3 üzerinde Object Lock yapılandırmasını tamamlayın.

Otomatik Uyarı ve Müdahale: alert_and_response.py dosyası ile saldırı tespitinde otomatik uyarılar ve müdahaleler yapın.
Kaynaklar

CICIDS Collection Dataset
Kaggle Cybersecurity Datasets

Katkıda Bulunanlar
[Sercan DOMAÇ] - Proje Yöneticisi ve Geliştirici
Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.
