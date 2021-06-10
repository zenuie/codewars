import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;


public class switcherooTest {
    @Test
    public void testSomething() {
        assertEquals("abc", switcheroo.Switcheroo("bac"));
        assertEquals("ccc", switcheroo.Switcheroo("ccc"));
        assertEquals("aaabcccbaaa", switcheroo.Switcheroo("bbbacccabbb"));
    }
}
