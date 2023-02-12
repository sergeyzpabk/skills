


def pars_all(_s:str, s:str , s_:str):
    result = []
    while (s.find(_s) != -1) and (s.find(s_) != -1):
        _pos =  s.find(_s)
        temp = s [ _pos + len(_s) : ]

        pos_ = temp.find(s_)
        result.append( s[ _pos + len(_s) : _pos + len(_s) + pos_ ] )

        s = s [: _pos] + s[ _pos + len(_s) + pos_ + len(s_):]

    return result

def pars(_s:str, s:str , s_:str):
    _pos =  s.find(_s)
    temp = s [ _pos + len(_s) : ]

    pos_ = temp.find(s_)
    return s[ _pos + len(_s) : _pos + len(_s) + pos_ ]


def parsProductHTML(html:str, url:str):
    """
        frame[0] код товара
        frame[1] категорий
        frame[2] наименование товара
        frame[3] наличие товара
        frame[4] цена
        frame[5] акционная цена
        frame[6] ссылка
        """
    frame = ['','','','','','','',]
    frame[6] = url

    #старая цена
    if html.find('<div class="price-main">') != -1:
        frame[4] = pars('<div class="price-main">',html,'<').strip().replace('₽','').replace(' ','')

    #обычная цена
    if html.find('<span class="pdp-sales-block__price-final">') !=-1:
        frame[4] = pars('<span class="pdp-sales-block__price-final">',html,'<').strip().replace('₽','').replace(' ','')

    #Акционнаяя цена
    if html.find('<span class="pdp-sales-block__discount-text">') != -1:
        price = pars('<div class="pdp-sales-block__old-price-small">', html,'<').strip().replace('₽','').replace(' ','')
        action = pars('<span class="pdp-sales-block__price-final">', html, '<').strip().replace('₽','').replace(' ','')
        frame[4] = price
        frame[5] = action

    if html.find('<button type="button" class="subscribe-button__btn btn sm btn-block">') != -1:
        frame[3] = 'Нет в наличии'
    else:
        frame[3] = 'В наличии'
    frame[0] = pars('Код товара:</span> <span itemprop="value">', html,'<')
    frame[2] = pars('class="pdp-header__title page-title">',html,'<')

    categories = pars_all('itemscope="itemscope"><span itemprop="name">', html,'<')
    frame[1] = '->'.join(categories)


    return frame

