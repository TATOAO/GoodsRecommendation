from Schema import GoodsRecUser, Good

if __name__ == "__main__":


    print('hellow')

    g1 = Good(id='1', cat4='A')
    g2 = Good(id='2', cat4='C')

    u1 = GoodsRecUser(aopsid="23423", city="cz", cart=['2131', '4234'], history_goods=['1', '2'])
    print(u1.history_goods)
