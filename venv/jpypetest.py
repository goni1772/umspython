from jpype import *
from flask import Flask, request
import requests

classpath = "./Lib/CASIFJAVACodec.jar"  # 경로 정의
startJVM(getDefaultJVMPath(), "-Djava.class.path=%s" % classpath)  # Python 내부에서 JVM 실행
DefaultExtractor = JPackage("com").lgtel.mmdb  # 암호화 패키지 정의
PyCasCryptoEncode = DefaultExtractor.CasCrypto.casCryptoEncode  # Encode Class.method 정의
PyCasCryptoDecode = DefaultExtractor.CasCrypto.casCryptoDecode  # Decode Class.method 정의

app = Flask(__name__)
@app.route('/')
def default():
    return 'please send CTN!'

@app.route('/getCASInfo', methods=['POST'])
def getCASInfo():
    CTN = request.form['CTN']
    enCTN = PyCasCryptoEncode("E645919BADBAD0D9", "D076AEABE5BC7585", "DF89BCE93B70CD13", "D91C3245767F1C0E", CTN)
    # +암호화 모듈 호출 =req
    # apiURL = "https://devcas.ez-i.co.kr/NIF/CASInterface.jsp?"
    # CASinfo = requests.get(URL)
    deCASinfo = PyCasCryptoDecode("E645919BADBAD0D9", "D076AEABE5BC7585", "DF89BCE93B70CD13", "D91C3245767F1C0E", enCTN)
    return (enCTN+deCASinfo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
