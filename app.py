import streamlit as st
from streamlit_chat import message
import random

# Configuration
if 'batas' not in st.session_state:
	st.session_state.batas = 0

if 'batas2' not in st.session_state:
	st.session_state.batas2 = 0

result = []
with open('generated-pantun-alpha.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith('<BOS>'):
            line_edit = line[5:]
            line_edit2 = line_edit.replace('  ', '')
            result.append(line_edit2.replace(r' \\n ', '\n'))
result = random.sample(result, len(result))


def check_akhiran_contoh(x):
  sajak1 = x[0][-1]
  sajak2 = x[1][-1]
  if sajak1 in ("a","i","u","e","o"):
    if sajak2 in ("a","i","u","e","o"):
      i3 = 1
      i4 = 1
      return sajak1, sajak2, i3, i4
    elif sajak2 in ('b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
      sajak2 = x[1][-2:]
      i3 = 1
      i4 = 2
      return sajak1, sajak2, i3, i4
    else:
      sajak2 = x[1][-3:]
      i3 = 1
      i4 = 3
      return sajak1, sajak2, i3, i4
  elif sajak1 in ('b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
    if sajak2 in ("a","i","u","e","o"):
      sajak1 = x[0][-2:]
      i3 = 2
      i4 = 1
      return sajak1, sajak2, i3, i4
    elif sajak2 in ('b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
      sajak1 = x[0][-2:]
      sajak2 = x[1][-2:]
      i3 = 2
      i4 = 2
      return sajak1, sajak2, i3, i4
    else:
      sajak1 = x[0][-2:]
      sajak2 = x[1][-3:]
      i3 = 2
      i4 = 3
      return sajak1, sajak2, i3, i4
  else:
    if sajak2 in ("a","i","u","e","o"):
      sajak1 = x[0][-3:]
      i3 = 3
      i4 = 1
      return sajak1, sajak2, i3, i4
    elif sajak2 in ('b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
      sajak1 = x[0][-3:]
      sajak2 = x[1][-2:]
      i3 = 3
      i4 = 2
      return sajak1, sajak2, i3, i4
    else:
      sajak1 = x[0][-3:]
      sajak2 = x[1][-3:]
      i3 = 3
      i4 = 3
      return sajak1, sajak2, i3, i4


def check_akhiran_prompt(x1,x2):
  sajak1 = x1[-1]
  sajak2 = x2[-1]
  if sajak1 in ("a","i","u","e","o"):
    if sajak2 in ("a","i","u","e","o"):
      i3 = 1
      i4 = 1
      return sajak1, sajak2, i3, i4
    elif sajak2 in ('b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
      sajak2 = x2[-2:]
      i3 = 1
      i4 = 2
      return sajak1, sajak2, i3, i4
    else:
      sajak2 = x2[-3:]
      i3 = 1
      i4 = 3
      return sajak1, sajak2, i3, i4
  elif sajak1 in ('b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
    if sajak2 in ("a","i","u","e","o"):
      sajak1 = x1[-2:]
      i3 = 2
      i4 = 1
      return sajak1, sajak2, i3, i4
    elif sajak2 in ('b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
      sajak1 = x1[-2:]
      sajak2 = x2[-2:]
      i3 = 2
      i4 = 2
      return sajak1, sajak2, i3, i4
    else:
      sajak1 = x1[-2:]
      sajak2 = x2[-3:]
      i3 = 2
      i4 = 3
      return sajak1, sajak2, i3, i4
  else:
    if sajak2 in ("a","i","u","e","o"):
      sajak1 = x1[-3:]
      i3 = 3
      i4 = 1
      return sajak1, sajak2, i3, i4
    elif sajak2 in ('b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
      sajak1 = x1[-3:]
      sajak2 = x2[-2:]
      i3 = 3
      i4 = 2
      return sajak1, sajak2, i3, i4
    else:
      sajak1 = x1[-3:]
      sajak2 = x2[-3:]
      i3 = 3
      i4 = 3
      return sajak1, sajak2, i3, i4

def on_input_change():
    batas = st.session_state.batas
    batas2 = st.session_state.batas2
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    inputan_split = user_input.split()
    print("")
    numbering = 1
    kata = ""
    baris_split = user_input.split("\n")

    if len(baris_split) == 2:
      if batas != 0 :
        # Agar batas output = 3
        berapa_banyak_output = 0
        baris_split = user_input.split("\n")
        baris3,baris4 = baris_split
        a, b, c, d = check_akhiran_prompt(baris3,baris4)
        for i in range(len(result)):
          pantun_ke = result[i].split('\n')
          if len(pantun_ke) >= 4 and pantun_ke[2] != "" and pantun_ke[3] != "":
            if pantun_ke[0][-c:] == a:
              if pantun_ke[1][-d:] == b:
                kata += (f"""===Pantun {numbering}===
{pantun_ke[0]}
{pantun_ke[1]}
{baris3}
{baris4}
""")
                numbering += 1
                st.session_state.batas -= st.session_state.batas
                berapa_banyak_output += 1
                if berapa_banyak_output == 3:
                  berapa_banyak_output = 0
                  break
              # else:
              #   continue
          else:
            continue
      elif batas2 != 0 :
        # Agar batas output = 3
        berapa_banyak_output = 0
        baris_split = user_input.split("\n")
        baris1,baris2 = baris_split
        a, b, c, d = check_akhiran_prompt(baris1,baris2)
        for i in range(len(result)):
          pantun_ke = result[i].split('\n')
          # print(pantun_ke)
          if len(pantun_ke) >= 4 and pantun_ke[2] != "" and pantun_ke[3] != "":
            if pantun_ke[2][-c:] == a:
              if pantun_ke[3][-d:] == b:
                kata+=(f"""===Pantun {numbering}===
{baris1}
{baris2}
{pantun_ke[2]}
{pantun_ke[3]}
""")
                numbering += 1
                st.session_state.batas2 -= st.session_state.batas2
                berapa_banyak_output += 1
                if berapa_banyak_output == 3:
                  berapa_banyak_output = 0
                  break
            #   else:
            #     continue
            # else:
            #   continue
          else:
            continue


    for xyz in inputan_split:
      if xyz.lower() == "contoh":
        flag = random.randint(0,len(result)-1)
        # Agar batas output = 5
        berapa_banyak_output = 0
        for i in range(1,len(result)):
          x = result[flag].split('\n')
          while True:
            if len(x) >= 4 and x[2] != "" and x[3] != "":
              break
            else:
              flag = random.randint(0,len(result)-1)
              x = result[flag].split('\n')
          a,b,c,d = check_akhiran_contoh(x)
          pantun_ke = result[i].split('\n')
          if len(pantun_ke) >= 4 and pantun_ke[2] != "" and pantun_ke[3] != "":
            if pantun_ke[2][-c:] == a:
              if pantun_ke[3][-d:] == b:
                kata += (f"""===Pantun {numbering}===
{x[0]}
{x[1]}
{pantun_ke[2]}
{pantun_ke[3]}

""")
                flag = random.randint(0,len(result)-1)
                numbering += 1
                berapa_banyak_output += 1
                if berapa_banyak_output == 5:
                  berapa_banyak_output = 0
                  break
            #   else:
            #     continue
            # else:
            #   continue
            else:
              flag = random.randint(0,len(result)-1)
      elif xyz.lower() == "sampiran":
        st.session_state.batas += 1
        kata+=("Tolong berikan isi, nanti saya akan memberikan anda sampiran")
      elif xyz.lower() == "isi":
        st.session_state.batas2 += 1
        kata+=("Tolong berikan sampiran, nanti saya akan memberikan anda isi")
    st.session_state.generated.append(f"{kata}")


def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]


st.session_state.setdefault('past', [])
st.session_state.setdefault('generated', [])

st.title("PANTUN GENERATOR by Ricky Khairul Faza")

chat_placeholder = st.empty()

with chat_placeholder.container():
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(st.session_state['generated'][i], key=f"{i}")

    st.button("Bersihkan Pesan", on_click=on_btn_click)

with st.container():
    st.text_area("User Input:", on_change=on_input_change, key="user_input")