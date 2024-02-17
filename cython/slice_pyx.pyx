# -*- coding:utf-8 -*-
# @FileName : slice_pyx.pyx.py
# @Time : 2024/2/17 13:21
# @Author : fiv
from functools import partial
from multiprocessing.pool import ThreadPool
from pydub import AudioSegment
from pydub.utils import make_chunks
from typing import Tuple, List
from pathlib import Path
from pydub import AudioSegment

def save(chunks: Tuple[int, AudioSegment], out_dir: Path) -> None:
    cdef int index
    chunk: AudioSegment
    index, chunk = chunks
    chunk_name: Path = out_dir / f"{index:02d}.wav"
    chunk.export(chunk_name, format="wav")

def slice_wav(wave_path: Path, slice_step: int = 30000) -> None:
    audio: AudioSegment = AudioSegment.from_file(wave_path, "wav")
    out_dir: Path = Path(__file__).parent / wave_path.stem
    out_dir.mkdir(parents=True, exist_ok=True)
    chunks: List[Tuple[int, AudioSegment]] = make_chunks(audio, slice_step)
    chunks = list(zip(range(len(chunks)), chunks))
    save_p = partial(save, out_dir=out_dir)

    with ThreadPool() as pool:
        pool.map(save_p, chunks)



# from cpython cimport array
# import numpy as np
# cimport cython
# from libc.stdlib cimport malloc, free
# from pydub import AudioSegment
# from pydub.utils import make_chunks
# from pathlib import Path
# from multiprocessing.pool import ThreadPool
# from functools import partial
#
# cdef class AudioSegmentWrapper:
#     cdef object audio_segment
#
#     def __cinit__(self, audio_segment):
#         if isinstance(audio_segment, AudioSegment):
#             self.audio_segment = audio_segment
#         else:
#             raise TypeError('Expected a AudioSegment object')
#
# cdef class PathWrapper:
#     cdef object path
#
#     def __cinit__(self, path):
#         self.path = Path(path)
#
# cdef void save(tuple chunks, PathWrapper out_dir):
#     cdef int index
#     cdef AudioSegmentWrapper chunk
#     index, chunk = chunks
#     cdef PathWrapper chunk_name = PathWrapper(out_dir.path / f"{index:02d}.wav")
#     chunk.audio_segment.export(chunk_name.path, format="wav")
#
# cpdef void slice_wav(PathWrapper wave_path, int slice_step=30000):
#     cdef AudioSegmentWrapper audio = AudioSegmentWrapper(AudioSegment.from_file(wave_path.path, "wav"))
#     cdef PathWrapper out_dir = PathWrapper(Path(__file__).parent / wave_path.path.stem)
#     out_dir.path.mkdir(parents=True, exist_ok=True)
#     cdef list chunks = [(i, AudioSegmentWrapper(chunk)) for i, chunk in
#                         enumerate(make_chunks(audio.audio_segment, slice_step))]
#     cdef save_p = partial(save, out_dir=out_dir)
#
#     with ThreadPool() as pool:
#         pool.map(save_p, chunks)
