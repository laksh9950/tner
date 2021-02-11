import os
import shutil
from glob import glob

for i in ['./ckpt/model_large', './ckpt/model_large_lower', './ckpt/model_base','./ckpt/model_base_lower']:
    prefix = '~/Projects/transformers_model_hub/tner-xlm-roberta'
    if 'large' in i:
        prefix += '-large'
    else:
        prefix += '-base'

    if 'lower' in i:
        prefix += '-uncased'

    for i_ in glob('{}/*'.format(i)):
        if os.path.isdir(i_):
            shutil.move('{}/*'.format(i_), prefix+'-'+os.path.basename(i_).replace('_', '-'))
            break
    break



# cp ${SRC}/config.json ${DST}/
# cp ${SRC}/special_tokens_map.json ${DST}/
# cp ${SRC}/pytorch_model.bin ${DST}/
# cp ${SRC}/sentencepiece.bpe.model ${DST}/
# cp ${SRC}/tokenizer_config.json ${DST}/