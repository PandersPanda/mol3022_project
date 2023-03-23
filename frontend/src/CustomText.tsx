
function CustomText(props: { t: string; }) {

    const inputText = props.t.split('');

    return <p>{inputText.map(inputText => {
        if (inputText.startsWith('H') || inputText.startsWith('h')) {
          return <span style={{ color: '#fb4f4f' }}>{inputText} </span>;
        } else if (inputText.startsWith('E') || inputText.startsWith('e')) {
          return <span style={{ color: '#6cc0e5' }}>{inputText} </span>;
        } else if (inputText.startsWith('C') || inputText.startsWith('c')) {
            return <span style={{ color: '#fbc93d' }}>{inputText} </span>;
        } else {
            return <span style={{ color: 'white' }}>{inputText} </span>;
        }
      })}</p>;
}

export default CustomText