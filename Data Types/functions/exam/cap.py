def cap(**kwargs):
    for k,v in kwargs.items():
        if isinstance(v,str):
            kwargs[k]=v.capitalize()
    print(kwargs)
cap(name='silpa',place='malappuram',course='python')