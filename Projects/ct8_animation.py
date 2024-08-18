import codesters

s1 = codesters.Sprite('doggo',-200,-200)
s1.set_size(.1)

for i in range(100):
    s1.say("test 123",1)
    s1.forward(10)
    stage.wait(1)
# answer = s1.ask("What is your name?")


print("Hello Codesters")
# print(answer)