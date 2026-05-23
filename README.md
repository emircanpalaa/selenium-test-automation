# Selenium and API Test Automation

SauceDemo UI testleri ve ReqRes API testleri icin hazirlanmis Python, Selenium, Requests ve Pytest tabanli test otomasyon projesidir.

Proje Page Object Model yapisini kullanir. UI tarafinda login, sepet, checkout ve urun islemleri test edilir. API tarafinda ReqRes uzerinden user, login, create, update ve delete senaryolari kontrol edilir.

## Ozellikler

- Selenium + Pytest ile UI test otomasyonu
- Requests + Pytest ile API test otomasyonu
- Page Object Model mimarisi
- Chrome ve Firefox tarayici destegi
- Headless test kosumu
- Paralel test calistirma destegi
- HTML rapor olusturma
- Allure result dosyalari uretme
- Basarisiz UI testlerinde otomatik screenshot alma
- GitHub Actions ile CI entegrasyonu
- API key icin environment variable ve GitHub Secrets kullanimi

## Kullanilan Teknolojiler

- Python 3.12
- Selenium
- Requests
- Pytest
- Pytest HTML
- Pytest Xdist
- WebDriver Manager
- Allure Pytest
- GitHub Actions

## Proje Yapisi

```text
.
|-- .github/
|   `-- workflows/
|       |-- api-test.yml
|       |-- test-pipeline.yml
|       `-- tests.yml
|-- api_tests/
|   |-- test_create_user_api.py
|   |-- test_delete_user_api.py
|   |-- test_login_api.py
|   |-- test_update_user_api.py
|   `-- test_users_api.py
|-- assets/
|   `-- style.css
|-- pages/
|   |-- base_page.py
|   |-- cart_page.py
|   |-- checkout_page.py
|   |-- inventory_page.py
|   `-- login_page.py
|-- tests/
|   |-- test_add_to_cart.py
|   |-- test_checkout.py
|   |-- test_invalid_checkout.py
|   |-- test_invalid_login.py
|   |-- test_login.py
|   |-- test_logout.py
|   |-- test_multiple_products.py
|   `-- test_remove_from_cart.py
|-- conftest.py
|-- requirements.txt
`-- README.md
```

## Kurulum

Proje dizinine gecin:

```powershell
cd "Selenium Proje"
```

Sanal ortam olusturun:

```powershell
python -m venv .venv
```

Windows PowerShell uzerinde sanal ortami aktif edin:

```powershell
.\.venv\Scripts\Activate.ps1
```

Bagimliliklari yukleyin:

```powershell
pip install -r requirements.txt
```

## ReqRes API Key

API testleri ReqRes API key ister. Key'i test dosyalarina veya workflow dosyasina direkt yazmayin. Local ortamda `REQRES_API_KEY` environment variable olarak tanimlayin.

Gecici olarak tanimlamak icin:

```powershell
$env:REQRES_API_KEY="your-api-key"
```

Kalici olarak tanimlamak icin:

```powershell
setx REQRES_API_KEY "your-api-key"
```

`setx` kullandiktan sonra VS Code terminalini kapatip yeniden acin.

## Testleri Calistirma

Tum testleri calistirmak icin:

```powershell
pytest
```

Sadece API testlerini calistirmak icin:

```powershell
pytest api_tests -q
```

Sadece UI testlerini calistirmak icin:

```powershell
pytest tests -q
```

Daha detayli cikti almak icin:

```powershell
pytest -v
```

Firefox ile UI testlerini calistirmak icin:

```powershell
pytest tests --browser firefox
```

Paralel test calistirmak icin:

```powershell
pytest -n auto
```

HTML rapor olusturmak icin:

```powershell
pytest -v --html=report.html --self-contained-html
```

Allure result dosyasi uretmek icin:

```powershell
pytest --alluredir=allure-results -v
```

## Test Kapsami

UI testleri:

- Gecerli kullanici ile login
- Gecersiz login senaryolari
- Sepete urun ekleme
- Sepetten urun cikarma
- Birden fazla urun ekleme
- Logout islemi
- Gecerli checkout akisi
- Eksik checkout bilgileriyle hata kontrolleri

API testleri:

- Kullanici bilgisi getirme
- Basarili login
- Eksik sifre ile login hata kontrolu
- Kullanici olusturma
- Kullanici guncelleme
- Kullanici silme

## GitHub Actions

GitHub Actions uzerinde API testlerinin calisabilmesi icin repo secret eklenmelidir.

GitHub uzerinde:

1. Repository sayfasina girin.
2. `Settings` sayfasini acin.
3. `Secrets and variables` > `Actions` alanina girin.
4. `New repository secret` secin.
5. Secret adini `REQRES_API_KEY` yapin.
6. ReqRes API key degerini secret value olarak kaydedin.

Workflow dosyalari:

- `.github/workflows/api-test.yml`: API testlerini calistirir.
- `.github/workflows/tests.yml`: Pytest suite'i calistirir ve HTML rapor uretir.
- `.github/workflows/test-pipeline.yml`: API ve UI testleri icin ayrilmis pipeline yapisidir.

Workflow icinde API key su sekilde okunur:

```yaml
env:
  REQRES_API_KEY: ${{ secrets.REQRES_API_KEY }}
```

## Raporlar ve Screenshot

HTML rapor olusturuldugunda proje kok dizininde `report.html` dosyasi uretilir.

Basarisiz UI testlerinde screenshot dosyalari su klasore kaydedilir:

```text
screenshots/
```

Allure result dosyalari su klasore yazilir:

```text
allure-results/
```

## Notlar

- UI testleri `https://www.saucedemo.com/` uzerinde calisir.
- API testleri `https://reqres.in/api` uzerinde calisir.
- API key'i kod icine yazmayin; localde environment variable, GitHub'da repository secret kullanin.
- `screenshots/`, `report.html`, `.pytest_cache/`, `__pycache__/`, `allure-results/` ve sanal ortam klasorleri git disinda tutulmalidir.
