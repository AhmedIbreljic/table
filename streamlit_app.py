import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

STREAMLIT_AGGRID_URL = "https://github.com/PablocFonseca/streamlit-aggrid"
st.set_page_config(
    layout="centered", page_icon="🖱️", page_title="EduX - [YOUR NAME]"
)
st.title("🖱️ EduX")
st.write(
    """Your updated degree audit for Fiscal Graduation Year XXXX. Our AI program found 0 changes in child-node calculations. 
    Class regression calculations reached a peak of 0.67 for your SOPHOMORE-year course selection. Your expected graduation time is 
    ahead of schedule compared to your CS-BA peers of 6 months."""
)


st.write("Go ahead, click on a row in the table below!")


def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.

    Args:
        df (pd.DataFrame): Source dataframe

    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="streamlit",  # Specify a valid theme option: "streamlit", "fresh", or "dark"
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection


iris = pd.read_csv(
    "https://raw.githubusercontent.com/AhmedIbreljic/table/main/eduxtest2.csv"
)

selection = aggrid_interactive_table(df=iris)

if selection:
    st.write("You selected:")
    st.json(selection["selected_rows"])

st.write("## Code")

st.code(
    '''
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

iris = pd.read_csv(
    "https://raw.githubusercontent.com/AhmedIbreljic/table/main/eduxtest2.csv"
)

def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.

    Args:
        df (pd.DataFrame): Source dataframe

    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="streamlit",  # Specify a valid theme option: "streamlit", "fresh", or "dark"
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection


iris = pd.read_csv(
    "https://raw.githubusercontent.com/AhmedIbreljic/table/main/eduxtest2.csv"
)

selection = aggrid_interactive_table(df=iris)

if selection:
    st.write("You selected:")
    st.json(selection["selected_rows"])
''',
    "python",
)
