import os

li = []
tmp = []

dataset = os.environ['dataset']
batch_info = os.environ['batch_info']
subj_id_list = os.environ['subj_id_list']
num_subj_batch = int(os.environ['num_subj_batch'])
print(num_subj_batch)
with open(subj_id_list, 'r') as f:
  for line in f:
    id_ = line.strip()
    tmp.append(id_)
    if len(tmp) == num_subj_batch:
      li.append(tmp.copy())
      tmp = []

li.append(tmp.copy())

num = 1
count = 0 # TEST_USE_ONLY
for l in li:
  with open(batch_info+'/id_batch_'+str(num), 'w') as f:
    body = '\n'.join(l)
    f.write(body)
  count+=len(l)

  num += 1

# print(count) #TEST_USE_ONLY
