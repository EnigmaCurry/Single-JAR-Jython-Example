import org.python.core.PyException;
import org.python.util.PythonInterpreter;

public class Main {
    public static void main(String[] args) throws PyException{
	PythonInterpreter intrp = new PythonInterpreter();
	intrp.exec("import excel_example");
	intrp.exec("excel_example.main()");
    }
}