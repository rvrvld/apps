import requests as r
import random
import os
import time as t
from faker import Faker
from fake_useragent import UserAgent as FUA
from dotenv import load_dotenv
import colorama
from colorama import Fore as x
green = x.GREEN
red = x.RED
blue = x.BLUE
reset = x.RESET
black = x.BLACK
yellow = x.YELLOW

load_dotenv()
colorama.init(autoreset=True)

class Instaddr:

    def __init__(self):
        self.api = r.Session()
        self.domain = os.getenv('DOMAIN')
        self.csrf = os.getenv('CSRF')
        self.hash = os.getenv('SESSIONHASH')
    
    def create_email(self, user):
        headers = {
            "Cookie":f'cookie_csrf_token={self.csrf}; cookie_sessionhash={self.hash}',
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        while True:
            try:
                return self.api.get(f"https://m.kuku.lu/index.php?action=addMailAddrByManual&nopost=1&by_system=1&t={int(t.time())}&csrf_token_check={self.csrf}&newdomain={self.domain}&newuser={user}&recaptcha_token=&_={int(t.time())}", headers=headers)
            except Exception as e:
                print(e)
                continue
    
    def check_email(self, email):
        headers = {
            "Cookie":f'cookie_csrf_token={self.csrf}; cookie_sessionhash={self.hash}',
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        while True:
            try:
                return self.api.get(f"https://m.kuku.lu/recv._ajax.php?&q={email}&&nopost=1&csrf_token_check={self.csrf}&csrf_subtoken_check=6d01b34752a27f4f8278ca03f5bef2b1&_={int(t.time())}", headers=headers)
            except Exception as e:
                print(e)
                continue
    
    def open(self, var, mail_data):
        data = f"num={var}&key={mail_data}&noscroll=1"
        headers = {
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie":f'cookie_csrf_token={self.csrf}; cookie_sessionhash={self.hash}',
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        while True:
            try:
                return self.api.post("https://m.kuku.lu/smphone.app.recv.view.php", data=data, headers=headers)
            except Exception as e:
                print(e)
                continue

class AppleID:

    def __init__(self):
        self.api = r.Session()
        self.sandi = "Gloria1404"
        self.proxy = os.getenv('PROXY')
    
    def prx(self):
        return self.proxy
    
    def headers(self, type, user_agent, cookie):
        headers = {
            "x-apple-store-front":"143476-2,8",
            "user-agent":user_agent,
            "content-type":type,
            "Origin":"https://music.apple.com",
            "Cookie":cookie
        }

        return headers
    
    def session(self, user_agent):
        while True:
            try:
                return self.api.get("https://auth.music.apple.com/auth/v1/liteReplayProtection/initializeSession", headers=self.headers("application/json", user_agent, "geo=ID;dslang=GB-EN;site=GBR"), proxies={"http": self.prx(), "https": self.prx()})
            except Exception as error:
                print(" ! " + red + str(error))
                continue
        
    def pod(self, user_agent, wosid_replay):
        while True:
            try:
                return self.api.get("https://buy.music.apple.com/account/pod", headers=self.headers("application/json", user_agent, f"geo=ID;dslang=GB-EN;site=IDN;wosid-replay={wosid_replay}"), proxies={"http": self.prx(), "https": self.prx()})
            except Exception as error:
                print(" ! " + red + str(error))
                continue

    def account_type(self, user_agent, wosid_replay, pod):
        while True:
            try:
                return self.api.get("https://buy.music.apple.com/account/restricted/create/options?restrictedAccountType=restrictedEmailOptimizedWeb", headers=self.headers("application/json", user_agent, f"geo=ID; dslang=GB-EN; site=IDN; wosid-replay={wosid_replay}; itspod={pod}"), proxies={"http": self.prx(), "https": self.prx()})
            except Exception as error:
                print(" ! " + red + str(error))
                continue
    
    def validate_account(self, user_agent, wosid_replay, pod, wosid_lite, page_type, email):
        data = f"storefront=IDN&pageUUID={page_type}&context=create&acAccountName={email}&acAccountPassword={self.sandi}&marketing=1&restrictedAccountType=restrictedEmailOptimizedWeb&addressOfficialCountryCode=IDN&paymentMethodType=None&accountType=email&email={email}"
        while True:
            try:
                return self.api.post("https://buy.music.apple.com/WebObjects/MZFinance.woa/wa/validateAccountFieldsSrv", data=data, headers=self.headers("application/x-www-form-urlencoded;charset=UTF-8", user_agent, f"geo=ID; dslang=GB-EN; site=IDN; wosid-replay={wosid_replay}; itspod={pod}; wosid-lite={wosid_lite}"), proxies={"http": self.prx(), "https": self.prx()})
            except Exception as error:
                print(" ! " + red + str(error))
                continue
    
    def validate_create(self, user_agent, wosid_replay, pod, wosid_lite, page_valid, email, first_name, last_name, ns, mzf, years, day, month):
        data = f"storefront=IDN&pageUUID={page_valid}&context=create&firstName={first_name}&lastName={last_name}&birthDay={day}&birthMonth={month}&birthYear={years}&acAccountName={email}&acAccountPassword={self.sandi}&restrictedAccountType=restrictedEmailOptimizedWeb&addressOfficialCountryCode=IDN&paymentMethodType=None&agreedToTerms=1&accountType=email&email={email}"
        while True:
            try:
                return self.api.post("https://buy.music.apple.com/WebObjects/MZFinance.woa/wa/validateAccountFieldsSrv", data=data, headers=self.headers("application/x-www-form-urlencoded;charset=UTF-8", user_agent, f"ns-mzf-inst={ns}; mzf_in={mzf}; geo=ID; dslang=GB-EN; site=IDN; wosid-replay={wosid_replay}; itspod={pod}; wosid-lite={wosid_lite}"), proxies={"http": self.prx(), "https": self.prx()})
            except Exception as error:
                print(" ! " + red + str(error))
                continue
    
    def send_otp(self, user_agent, wosid_replay, wosid_lite, pod, ns, mzf, email):
        data = {
            "email":email
        }

        while True:
            try:
                return self.api.post("https://buy.music.apple.com/WebObjects/MZFinance.woa/wa/generateEmailConfirmationCodeSrv", json=data, headers=self.headers("application/json", user_agent, f"ns-mzf-inst={ns}; mzf_in={mzf}; geo=ID; dslang=GB-EN; site=IDN; wosid-replay={wosid_replay}; itspod={pod}; wosid-lite={wosid_lite}"), proxies={"http": self.prx(), "https": self.prx()})
            except Exception as error:
                print(" ! " + red + str(error))
                continue
    
    def validate_otp(self, user_agent, wosid_replay, pod, wosid_lite, ns, mzf, email, otp, client_token):
        data = {
            "email":email,
            "secretCode":otp,
            "clientToken":client_token
        }
        while True:
            try:
                return self.api.post("https://buy.music.apple.com/WebObjects/MZFinance.woa/wa/validateEmailConfirmationCodeSrv", json=data, headers=self.headers("application/json", user_agent, f"ns-mzf-inst={ns}; mzf_in={mzf}; geo=ID; dslang=GB-EN; site=IDN; wosid-replay={wosid_replay}; itspod={pod}; wosid-lite={wosid_lite}"), proxies={"http": self.prx(), "https": self.prx()})
            except Exception as error:
                print(" ! " + red + str(error))
                continue
    
    def create_account(self, wosid_replay, pod, wosid_lite, ns, mzf, email, first_name, last_name, page_token, day, month, years, otp, client_token):
        data=f"storefront=IDN&pageUUID={page_token}&context=create&firstName={first_name}&lastName={last_name}&birthDay={day}&birthMonth={month}&birthYear={years}&acAccountName={email}&acAccountPassword={self.sandi}&restrictedAccountType=restrictedEmailOptimizedWeb&addressOfficialCountryCode=IDN&paymentMethodType=None&agreedToTerms=1&accountType=email&email={email}&secretCode={otp}&clientToken={client_token}&webCreate=False"
        while True:
            try:
                return self.api.post("https://buy.music.apple.com/WebObjects/MZFinance.woa/wa/createAccountSrv", data=data, headers=self.headers("application/x-www-form-urlencoded;charset=UTF-8", user_agent, f"ns-mzf-inst={ns}; mzf_in={mzf}; geo=ID; dslang=GB-EN; site=IDN; wosid-replay={wosid_replay}; itspod={pod}; wosid-lite={wosid_lite}"), proxies={"http": self.prx(), "https": self.prx()})
            except Exception as error:
                print(" ! " + red + str(error))
                continue



faker = Faker()
utils = AppleID()
mail = Instaddr()

os.system('cls' if os.name == "nt" else 'clear')

print(
    f"""
      O)                        O))            O))O)))))    
     O) ))                      O))            O))O))   O)) 
    O)  O))    O) O))  O) O))   O))   O))      O))O))    O))   {yellow}AppleID Creator{reset}
   O))   O))   O)  O)) O)  O))  O)) O)   O))   O))O))    O))       {blue}t.me/chsangkara{reset}
  O)))))) O))  O)   O))O)   O)) O))O))))) O))  O))O))    O))
 O))       O)) O)) O)) O)) O))  O))O)          O))O))   O)) 
O))         O))O))     O))     O)))  O))))     O))O)))))    
               O))     O))                                
"""
)

while True:
    while True:
        user = faker.user_name().replace(" ","").lower() + str(random.randint(100,999))
        while True:
            try:
                email = mail.create_email(user)
                if "@" in email.text:
                    email = email.text.split("OK:")[1]
                    print(" ! " + green + "Your email address " + email)
                    break
                else:
                    continue
            except Exception as e:
                print(e)
                continue
        # email = input(yellow + " ! Enter your email address : " + reset)
        user_agent = FUA().random
        purge_cookies = utils.session(user_agent)
        try:
            wosid_replay = purge_cookies.headers.get("Set-Cookie").split('wosid-replay=')[1].split(';')[0]
            # print(" ! " + green + wosid_replay)
        except Exception as error:
            print(" ! " + red + str(error))
            continue
        
        call_pod = utils.pod(user_agent, wosid_replay)
        try:
            if call_pod.status_code == 204:
                pod = call_pod.headers.get("set-cookie").split("itspod=")[1].split(";")[0]
                print(" ! POD V1 : " + green + pod + ' | ' + wosid_replay)
            else:
                continue
        except Exception as error:
            print(" ! " + red + str(error))
            continue

        call_type = utils.account_type(user_agent, wosid_replay, pod)
        try:
            page_type = call_type.json()["pageUUID"]
            wosid_lite = call_type.headers.get("set-cookie").split("wosid-lite=")[1].split(";")[0]
            print(" ! POD V2 : " + green + pod + ' | ' + wosid_lite)
        except Exception as e:
            print(" ! " + red + str(e))
            continue

        call_validate_account = utils.validate_account(user_agent, wosid_replay, pod, wosid_lite, page_type, email)
        try:
            if "pageUUID" in call_validate_account.text:
                page_valid = call_validate_account.json()["pageUUID"]
                ns = call_validate_account.headers.get("set-cookie").split("ns-mzf-inst=")[1].split(";")[0]
                mzf = call_validate_account.headers.get("set-cookie").split("mzf_in")[1].split(";")[0]
                print("\n ! " + green + ns)
                break
            else:
                if call_validate_account.json()["status"] == -1:
                    print(" ! " + red + "Account validate V1 failed confirm\n")
                continue
        except Exception as e:
            print(" ! " + red + str(e))
            continue
    
    first_name = faker.user_name()
    last_name = faker.user_name()
    years = str(random.randint(1997,2003))
    day = str(random.randint(10,30))
    month = str(random.randint(10,12))

    while True:
        call_verify = utils.validate_create(user_agent, wosid_replay, pod, wosid_lite, page_valid, email, first_name, last_name, ns, mzf, years, day, month)
        try:
            if "pageUUID" in call_verify.text:
                break
            else:
                if call_verify.json()["status"] == -1:
                    print(" ! " + red + "Account validate V2 failed confirm")
                continue
        except Exception as e:
            print(" ! " + red + str(e))
            continue
    
    send = utils.send_otp(user_agent, wosid_replay, wosid_lite, pod, ns, mzf, email)
    if "clientToken" in send.text:
        client_token = send.json()["clientToken"]
        print(" ! " + green + "Sending otp succeded !")
    else:
        exit(" ! " + red + " Sending otp failed confirm")
    
    while True:
        while True:
            cek_email = mail.check_email(email)
            if "Apple" in cek_email.text:
                var = cek_email.text.split("openMailData('")[1].split("',")[0]
                mail_data = cek_email.text.split(f"openMailData('{var}', '")[1].split("',")[0]
                otp = mail.open(var, mail_data).text.split("<p><b>")[1].split("</b></p></div>")[0]
                break
            else:
                continue
        # otp = input(black + "\n ! Enter your otp : ")
        verify = utils.validate_otp(user_agent, wosid_replay, pod, wosid_lite, ns, mzf, email, otp, client_token)
        try:
            if "pageUUID" in verify.text:
                page_token = verify.json()["pageUUID"]
                print(" ! " + green + "Code Validation Success")
                break
            else:
                continue
        except Exception as e:
            print(" ! " + red + str(error))
            continue
    
    sign = utils.create_account(wosid_replay, pod, wosid_lite, ns, mzf, email, first_name, last_name, page_token, day, month, years, otp, client_token)
    try:
        if sign.json()["status"] == 0:
            print(" ! " + green + "Account succeded create\n")
            with open('appleid.txt', 'a') as f:
                f.write(f"EMAIL : {email} | SANDI : @Satuduatiga45 | CREATED : True\n")
        else:
            print(" ! " + red + "Account failed create\n")
    except Exception as error:
        continue
