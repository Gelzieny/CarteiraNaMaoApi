import re

just_numbers = lambda a: ''.join(re.findall("\d+", a))

def retira_vazios(param):
  ret = {}
  for i in param:
    if not (len(str(param[i])) == 0  or param[i] is None):
      ret.update({i: param[i]})

  return ret