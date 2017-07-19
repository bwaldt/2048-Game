import GameManager

if __name__ == '__main__':
    results =[]
    for x in xrange(1):
        res = GameManager.main()
        print res
        results.append(res)
    print results