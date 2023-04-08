import requests

url = "https://pje.trt4.jus.br/pje-certidoes-api/api/certidoes/trabalhistas/emissao"

payload = {
    "criterioDeEmissao": "CPF",
    "nome": "",
    "numeroDoDocumento": "125.015.044-29",
    "respostaDoCaptcha": "03AKH6MREMwZmBnLMplH2_J7ydCAhhDZuMSRZ_WfnmoBXbPHGVUi1l0pp1JKxEwsUtzHAKuQS9xP0x-fLXEAE2y_PjMrJ--QoN0qDT36mZysClsS7Z1QdFQwVkylvq1d4nVNq8l9n4jphzHJ9hnpw1xOIueGpG5RM7wVkcte9D1x6e10bTD5r6Zuz8HtXmlxfMqPMEYd1RdfYZLau53U0N9vdY8oiQKCCunDBlJH7onbSE_CLwCsbi8NHo5HjjvxHlGxIc1GTY7hcSUooKWEF_2_kf2_Y2cESdTP1QbliMFrbdMHhqA4Z17x7cBF79vEw0EvvqSWnmYZoVhi8o7nIF8qs11GwRZK52-CLQWXHKda5ezCoV2xrYT5-SwZ3Br3pmpLsDWE8q9F-gBU2W_OHosuJRbSDhricHLurnptZUrJAzMuoUBBK94mTl4lr2Vyio947UzWMIq1tXFruPn1TrYriJv6jt5HUOrL3TKNQti9xAEJQ9gi2l2ZKkSqrPZo2-fdcsRmj602PLbl3uqYyBuQp4iAEXGe5_-yQNgj82icfXmAO6LCTx3AQ",
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "pje.trt4.jus.br",
    "Origin": "https://pje.trt4.jus.br",
    "Referer": "https://pje.trt4.jus.br/pje-consulta-api/",
    "TE": "Trailers",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}

response = requests.post(url, json=payload, headers=headers)
html_content = response.text
print(html_content)


#https://www.google.com/recaptcha/api2/userverify?k=6LeFj3QaAAAAAIhQt27bGh0XQks00PmVXz_kYQRN
                                                   #6LeFj3QaAAAAAIhQt27bGh0XQks00PmVXz_kYQRN

#03AKH6MRF8-k5edKdszB0Vwdt-HnRZzNNS7tplYA8Pb4xB6cBQehS4syLVGnD0VaTHk7BkKIogwJ2PZdPgBEYgalVapp_61PvTQhb-w0o9w-e8Uq4fz9wMiJkDD1pIBMZy1BzBh4F0mJSZUeK3jjWRsj_1sdMjVoRRGGqVveDH1J0XMDwYlTNJ7O97qgPbSfn0ld7m3zM61N8xsRUMWlCMOHxroGLWEfAU6qXG8b5S6D3mPyXziftvirLPi3ZXD1FGa2DMGEpZG0CgmWi3NHJH-RDNU7zFF_0Vv4Ds5A6oQ8i7ib_8IqCviTxnSyxyDHBGObvxHBXYFvJxC5NJXqzWQK-1LND2zo05e7CrcdBDu11c6BLIRjtiJfW5fvhMQHf2NNHPRV79nbaKS7LqCJtPd_VV16cyVoMLf7BmTLGJRngEoIE6m3JKlANpu2k8sfCL1wCO8mlMw45kdkwi9eEKlXy4yzfxgjfMUvQuijdCt-0YWOmKVWqFnWO5666Sk5uZ5xNdmKOZ0Sv2czXHsLC8Q4B0IZojfCUwc033jmox__LqCTrF_T2JSbo
#03AKH6MRF8-k5edKdszB0Vwdt-HnRZzNNS7tplYA8Pb4xB6cBQehS4syLVGnD0VaTHk7BkKIogwJ2PZdPgBEYgalVapp_61PvTQhb-w0o9w-e8Uq4fz9wMiJkDD1pIBMZy1BzBh4F0mJSZUeK3jjWRsj_1sdMjVoRRGGqVveDH1J0XMDwYlTNJ7O97qgPbSfn0ld7m3zM61N8xsRUMWlCMOHxroGLWEfAU6qXG8b5S6D3mPyXziftvirLPi3ZXD1FGa2DMGEpZG0CgmWi3NHJH-RDNU7zFF_0Vv4Ds5A6oQ8i7ib_8IqCviTxnSyxyDHBGObvxHBXYFvJxC5NJXqzWQK-1LND2zo05e7CrcdBDu11c6BLIRjtiJfW5fvhMQHf2NNHPRV79nbaKS7LqCJtPd_VV16cyVoMLf7BmTLGJRngEoIE6m3JKlANpu2k8sfCL1wCO8mlMw45kdkwi9eEKlXy4yzfxgjfMUvQuijdCt-0YWOmKVWqFnWO5666Sk5uZ5xNdmKOZ0Sv2czXHsLC8Q4B0IZojfCUwc033jmox__LqCTrF_T2JSbo


