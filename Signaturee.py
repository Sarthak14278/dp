#create_keys
!pip install rsa
import rsa
public_key,private_key=rsa.newkeys(2048)
with open('public_key_file.pem','wb') as puk:
    puk.write(public_key.save_pkcs1('PEM'))
with open('private_key_file.pem','wb') as prk:
    prk.write(private_key.save_pkcs1('PEM'))

#sign
import rsa
with open('samplepdf.pdf','rb') as f:
    pdf=f.read()
with open('private_key_file.pem','rb') as pr:
    private_key=rsa.PrivateKey.load_pkcs1(pr.read())
signature_file=rsa.sign(pdf,private_key,'SHA-256')
print(len(signature_file))
with open('signature_file','wb') as sf:
    sf.write(signature_file)

#verify
import rsa
with open('samplepdf.pdf','rb') as f:
    pdf=f.read()
with open('public_key_file.pem','rb') as puk:
    public_key=rsa.PublicKey.load_pkcs1(puk.read())
with open('signature_file','rb') as sf:
    signature_file=sf.read()
verify_file=rsa.verify(pdf,signature_file,public_key)
verify_file
