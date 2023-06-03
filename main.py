from dict import MORSE_CODE_DICT

message = input('What is your message?').upper()

output = []

for letter in message:
    m_letter = MORSE_CODE_DICT[letter]
    output.append(m_letter)

print(output)
