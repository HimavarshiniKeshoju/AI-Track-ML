import math
x_o=2
y_o=5
eta=0.01
eps=0.000001
del_x=1
del_y=1
max_iters=100
iters=0
def deriv(x,y):
    #e=2.71
    x_deriv=6*(x)
    b=math.exp(-y)
    y_deriv=5*b
    return x_deriv,y_deriv
while max(abs(del_x),abs(del_y))>eps and iters < max_iters:
    prev_x=x_o
    prev_y=y_o
    del_x,del_y=deriv(prev_x,prev_y)
    del_x=-eta *del_x
    del_y=-eta *del_y
    x_o=x_o+del_x
    y_o=y_o+del_y
    iters=iters+1
    print("Iteration",iters,"\nX value is",x_o,"\nY value is",y_o)
print("The local minimum occurs at",x_o,y_o)
    


"""OUTPUT
Iteration 1 
X value is 1.88 
Y value is 4.999663102650046
Iteration 2 
X value is 1.7671999999999999 
Y value is 4.999326091781146
Iteration 3 
X value is 1.661168 
Y value is 4.99898896731678
Iteration 4 
X value is 1.5614979199999999 
Y value is 4.9986517291803505
Iteration 5 
X value is 1.4678080448 
Y value is 4.998314377295181
Iteration 6 
X value is 1.3797395621119999 
Y value is 4.997976911584518
Iteration 7 
X value is 1.29695518838528 
Y value is 4.997639331971531
Iteration 8 
X value is 1.219137877082163 
Y value is 4.997301638379311
Iteration 9 
X value is 1.1459896044572333 
Y value is 4.996963830730873
Iteration 10 
X value is 1.0772302281897992 
Y value is 4.9966259089491505
Iteration 11 
X value is 1.0125964144984112 
Y value is 4.9962878729570015
Iteration 12 
X value is 0.9518406296285066 
Y value is 4.995949722677205
Iteration 13 
X value is 0.8947301918507962 
Y value is 4.995611458032461
Iteration 14 
X value is 0.8410463803397484 
Y value is 4.995273078945393
Iteration 15 
X value is 0.7905835975193636 
Y value is 4.9949345853385445
Iteration 16 
X value is 0.7431485816682017 
Y value is 4.994595977134379
Iteration 17 
X value is 0.6985596667681097 
Y value is 4.9942572542552846
Iteration 18 
X value is 0.6566460867620231 
Y value is 4.9939184166235675
Iteration 19 
X value is 0.6172473215563017 
Y value is 4.993579464161456
Iteration 20 
X value is 0.5802124822629235 
Y value is 4.9932403967911005
Iteration 21 
X value is 0.5453997333271481 
Y value is 4.99290121443457
Iteration 22 
X value is 0.5126757493275192 
Y value is 4.992561917013856
Iteration 23 
X value is 0.4819152043678681 
Y value is 4.9922225044508695
Iteration 24 
X value is 0.453000292105796 
Y value is 4.991882976667442
Iteration 25 
X value is 0.42582027457944827 
Y value is 4.991543333585327
Iteration 26 
X value is 0.4002710581046814 
Y value is 4.991203575126197
Iteration 27 
X value is 0.3762547946184005 
Y value is 4.9908637012116435
Iteration 28 
X value is 0.35367950694129646 
Y value is 4.9905237117631795
Iteration 29 
X value is 0.33245873652481867 
Y value is 4.990183606702239
Iteration 30 
X value is 0.31251121233332957 
Y value is 4.989843385950173
Iteration 31 
X value is 0.2937605395933298 
Y value is 4.9895030494282535
Iteration 32 
X value is 0.27613490721773004 
Y value is 4.989162597057674
Iteration 33 
X value is 0.25956681278466626 
Y value is 4.988822028759545
Iteration 34 
X value is 0.24399280401758627 
Y value is 4.988481344454897
Iteration 35 
X value is 0.2293532357765311 
Y value is 4.988140544064681
Iteration 36 
X value is 0.21559204162993925 
Y value is 4.987799627509765
Iteration 37 
X value is 0.2026565191321429 
Y value is 4.987458594710938
Iteration 38 
X value is 0.1904971279842143 
Y value is 4.9871174455889085
Iteration 39 
X value is 0.17906730030516144 
Y value is 4.9867761800643
Iteration 40 
X value is 0.16832326228685174 
Y value is 4.986434798057659
Iteration 41 
X value is 0.15822386654964063 
Y value is 4.986093299489449
Iteration 42 
X value is 0.14873043455666218 
Y value is 4.985751684280051
Iteration 43 
X value is 0.13980660848326246 
Y value is 4.985409952349766
Iteration 44 
X value is 0.1314182119742667 
Y value is 4.985068103618813
Iteration 45 
X value is 0.1235331192558107 
Y value is 4.9847261380073284
Iteration 46 
X value is 0.11612113210046206 
Y value is 4.984384055435368
Iteration 47 
X value is 0.10915386417443433 
Y value is 4.984041855822904
Iteration 48 
X value is 0.10260463232396827 
Y value is 4.983699539089826
Iteration 49 
X value is 0.09644835438453017 
Y value is 4.983357105155944
Iteration 50 
X value is 0.09066145312145836 
Y value is 4.983014553940984
Iteration 51 
X value is 0.08522176593417086 
Y value is 4.982671885364589
Iteration 52 
X value is 0.0801084599781206 
Y value is 4.98232909934632
Iteration 53 
X value is 0.07530195237943337 
Y value is 4.981986195805654
Iteration 54 
X value is 0.07078383523666737 
Y value is 4.981643174661989
Iteration 55 
X value is 0.06653680512246733 
Y value is 4.981300035834636
Iteration 56 
X value is 0.06254459681511929 
Y value is 4.980956779242824
Iteration 57 
X value is 0.058791921006212125 
Y value is 4.9806134048057
Iteration 58 
X value is 0.0552644057458394 
Y value is 4.980269912442327
Iteration 59 
X value is 0.05194854140108904 
Y value is 4.979926302071684
Iteration 60 
X value is 0.048831628917023695 
Y value is 4.979582573612667
Iteration 61 
X value is 0.045901731182002276 
Y value is 4.979238726984089
Iteration 62 
X value is 0.04314762731108214 
Y value is 4.978894762104678
Iteration 63 
X value is 0.040558769672417214 
Y value is 4.978550678893079
Iteration 64 
X value is 0.03812524349207218 
Y value is 4.978206477267852
Iteration 65 
X value is 0.03583772888254785 
Y value is 4.977862157147475
Iteration 66 
X value is 0.033687465149594975 
Y value is 4.977517718450339
Iteration 67 
X value is 0.03166621724061928 
Y value is 4.977173161094753
Iteration 68 
X value is 0.02976624420618212 
Y value is 4.976828484998941
Iteration 69 
X value is 0.027980269553811193 
Y value is 4.976483690081041
Iteration 70 
X value is 0.026301453380582523 
Y value is 4.976138776259108
Iteration 71 
X value is 0.02472336617774757 
Y value is 4.975793743451112
Iteration 72 
X value is 0.023239964207082717 
Y value is 4.975448591574937
Iteration 73 
X value is 0.021845566354657755 
Y value is 4.975103320548383
Iteration 74 
X value is 0.02053483237337829 
Y value is 4.974757930289165
Iteration 75 
X value is 0.019302742430975593 
Y value is 4.974412420714912
Iteration 76 
X value is 0.018144577885117058 
Y value is 4.974066791743168
Iteration 77 
X value is 0.017055903212010035 
Y value is 4.97372104329139
Iteration 78 
X value is 0.01603254901928943 
Y value is 4.973375175276953
Iteration 79 
X value is 0.015070596078132065 
Y value is 4.973029187617143
Iteration 80 
X value is 0.014166360313444142 
Y value is 4.972683080229161
Iteration 81 
X value is 0.013316378694637494 
Y value is 4.972336853030122
Iteration 82 
X value is 0.012517395972959243 
Y value is 4.971990505937057
Iteration 83 
X value is 0.011766352214581688 
Y value is 4.971644038866906
Iteration 84 
X value is 0.011060371081706787 
Y value is 4.971297451736527
Iteration 85 
X value is 0.01039674881680438 
Y value is 4.970950744462691
Iteration 86 
X value is 0.009772943887796117 
Y value is 4.97060391696208
Iteration 87 
X value is 0.00918656725452835 
Y value is 4.970256969151293
Iteration 88 
X value is 0.00863537321925665 
Y value is 4.9699099009468375
Iteration 89 
X value is 0.008117250826101251 
Y value is 4.969562712265138
Iteration 90 
X value is 0.007630215776535176 
Y value is 4.96921540302253
Iteration 91 
X value is 0.007172402829943065 
Y value is 4.968867973135263
Iteration 92 
X value is 0.006742058660146481 
Y value is 4.968520422519498
Iteration 93 
X value is 0.006337535140537693 
Y value is 4.96817275109131
Iteration 94 
X value is 0.005957283032105431 
Y value is 4.967824958766685
Iteration 95 
X value is 0.005599846050179105 
Y value is 4.967477045461522
Iteration 96 
X value is 0.005263855287168359 
Y value is 4.967129011091632
Iteration 97 
X value is 0.0049480239699382575 
Y value is 4.966780855572739
Iteration 98 
X value is 0.004651142531741962 
Y value is 4.966432578820477
Iteration 99 
X value is 0.0043720739798374444 
Y value is 4.966084180750395
Iteration 100 
X value is 0.004109749541047198 
Y value is 4.96573566127795
The local minimum occurs at 0.004109749541047198 4.96573566127795

"""