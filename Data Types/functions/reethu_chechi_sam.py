def fn1(**kwargs):
    print("audi speed and bmw color :",kwargs['audi'][6:-10],kwargs['bmw'][16:])
fn1(audi='speed_250,color_red', bmw='speed_200,color_black',mb='speed_190,color_white')

def fn2(*args):
    print("audi speed :",args[0][6:-10])
    print("bmw color :", args[1][16:])
fn2('speed_250,color_red','speed_200,color_black','speed_190,color_white')