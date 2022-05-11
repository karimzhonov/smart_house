import json
import pandas as pd
import streamlit as st

from smart_home.consumer import Consumer

__all__ = ['WebInterface']


class WebInterface:
    def __init__(self):
        self.cons = Consumer()

    def run(self):
        dev_dict = {}

        with st.empty():
            for msg in self.cons:
                msg_dict = json.loads(msg.value.decode('utf-8'))
                if msg_dict.get("msg_type") == "data":
                    dev_dict[msg_dict["dev"]["id"]] = {"id": msg_dict["dev"]["id"],
                                                       "dev_name": msg_dict["dev"]["dev_name"],
                                                       "type": msg_dict["dev"]["type"],
                                                       "dt": msg_dict["dt"],
                                                       "data": msg_dict["data"],
                                                       "room": msg_dict["info"]["room"],
                                                       "floor": msg_dict["info"]["floor"]}
                    df = pd.DataFrame([dev_dict[i] for i in sorted(list(dev_dict.keys()))])
                    st.write(df)
