from typing import MutableMapping, MutableSequence, Hashable, IO, Text
from werkzeug.datastructures import FileStorage
import hashlib

def generate_hash(fs: IO) -> MutableMapping[Text, Text]:
    return {"sha1": (hash_value := str(hashlib.sha1(fs.read()).hexdigest())), "short_hash": hash_value[0:6]}

def get_hashes(f_arr: MutableSequence[FileStorage]) -> MutableMapping[Text, Text]:
    return [{"filename": f.filename, **generate_hash(f.stream)} for f in f_arr]
