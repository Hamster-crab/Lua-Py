function sampleplus()
 b = io.read()
 c = c + b
end

function sampleminus()
 b = io.read()
 c = c - b
end

function samplekakeru()
 b = io.read()
 c = c * b
end

function samplewaru()
 b = io.read()
 c = c / b
end

local function sleep()
  local start = os.time()
  while os.time() - start < 1 do end
end 


print ("最初は何？(半角数字で)")
c = io.read()

while true do
 print (" + , - , * , / または、 = , exit , reset ")
 a = io.read()
 if a=="+" then
  sampleplus()
 elseif a=="-" then
  sampleminus()
 elseif a=="*" then
  samplekakeru()
 elseif a=="/" then
  samplewaru()
 elseif a=="=" then
  print(c)
  for i=1,5 do
   sleep()
  end
  error()
 elseif a=="exit" then
  break
 elseif a=="reset" then
  b = 0
  c = 0    
 end
end