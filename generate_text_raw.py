import tensorflow as tf

text = input("Input word to start your AI prediction with: ")

one_step_reloaded = tf.saved_model.load('one_step')
states = None
next_char = tf.constant([text])
result = [next_char]

for _ in range(100):
    next_char, states = one_step_reloaded.generate_one_step(next_char, states_=states)
    result.append(next_char)

print(tf.strings.join(result)[0].numpy().decode("utf-8"))
